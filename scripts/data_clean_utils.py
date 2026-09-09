import numpy as np
import pandas as pd

columns_to_drop = [
    'rider_id', 'restaurant_latitude', 'restaurant_longitude', 
    'delivery_latitude', 'delivery_longitude', 'order_date', 
    "order_time_hour", "order_day", "city_name", 
    "order_day_of_week", "order_month"
]

def change_column_names(data: pd.DataFrame):
    return (
        data.rename(str.lower, axis=1)
        .rename({
            "delivery_person_id": "rider_id",
            "delivery_person_age": "age",
            "delivery_person_ratings": "ratings",
            "delivery_location_latitude": "delivery_latitude",
            "delivery_location_longitude": "delivery_longitude",
            "time_orderd": "order_time",
            "time_order_picked": "order_picked_time",
            "weatherconditions": "weather",
            "road_traffic_density": "traffic",
            "city": "city_type"
        }, axis=1)
    )

def time_of_day(ser):
    return pd.cut(ser, bins=[0, 6, 12, 17, 20, 24], right=True,
                  labels=["after_midnight", "morning", "afternoon", "evening", "night"])

def data_cleaning(data: pd.DataFrame):
    minors_data = data.loc[data['age'].astype('float') < 18]
    minor_index = minors_data.index.tolist()
    six_star_data = data.loc[data['ratings'] == "6"]
    six_star_index = six_star_data.index.tolist()

    return (
        data
        .drop(columns="id", errors='ignore')
        .drop(index=minor_index)
        .drop(index=six_star_index)
        .replace("NaN ", np.nan)
        .assign(
            city_name=lambda x: x['rider_id'].str.split("RES").str.get(0),
            age=lambda x: x['age'].astype(float),
            ratings=lambda x: x['ratings'].astype(float),
            restaurant_latitude=lambda x: x['restaurant_latitude'].abs(),
            restaurant_longitude=lambda x: x['restaurant_longitude'].abs(),
            delivery_latitude=lambda x: x['delivery_latitude'].abs(),
            delivery_longitude=lambda x: x['delivery_longitude'].abs(),
            order_date=lambda x: pd.to_datetime(x['order_date'], dayfirst=True),
            order_day=lambda x: x['order_date'].dt.day,
            order_month=lambda x: x['order_date'].dt.month,
            order_day_of_week=lambda x: x['order_date'].dt.day_name().str.lower(),
            is_weekend=lambda x: x['order_date'].dt.day_name().isin(["Saturday", "Sunday"]).astype(int),
            order_time=lambda x: pd.to_datetime(x['order_time'], format='mixed', errors='coerce'),
            order_picked_time=lambda x: pd.to_datetime(x['order_picked_time'], format='mixed', errors='coerce'),
            pickup_time_minutes=lambda x: (x['order_picked_time'] - x['order_time']).dt.seconds / 60,
            order_time_hour=lambda x: x['order_time'].dt.hour,
            order_time_of_day=lambda x: x['order_time_hour'].pipe(time_of_day),
            weather=lambda x: x['weather'].str.replace("conditions ", "").str.lower().replace("nan", np.nan),
            traffic=lambda x: x["traffic"].str.rstrip().str.lower(),
            type_of_order=lambda x: x['type_of_order'].str.rstrip().str.lower(),
            type_of_vehicle=lambda x: x['type_of_vehicle'].str.rstrip().str.lower(),
            festival=lambda x: x['festival'].str.rstrip().str.lower(),
            city_type=lambda x: x['city_type'].str.rstrip().str.lower(),
            multiple_deliveries=lambda x: x['multiple_deliveries'].astype(float)
        )
        .drop(columns=["order_time", "order_picked_time"])
    )

def clean_lat_long(data: pd.DataFrame, threshold=1):
    location_columns = ['restaurant_latitude', 'restaurant_longitude',
                        'delivery_latitude', 'delivery_longitude']
    return (
        data.assign(**{
            col: np.where(data[col] < threshold, np.nan, data[col].values)
            for col in location_columns
        })
    )

def calculate_haversine_distance(df):
    lon1, lat1, lon2, lat2 = map(np.radians, [
        df['restaurant_longitude'], df['restaurant_latitude'], 
        df['delivery_longitude'], df['delivery_latitude']
    ])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat / 2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    
    return df.assign(distance=6371 * c)

def create_distance_type(data: pd.DataFrame):
    return data.assign(
        distance_type=pd.cut(data["distance"], bins=[0, 5, 10, 15, 25],
                             right=False, labels=["short", "medium", "long", "very_long"])
    )

def perform_data_cleaning(data: pd.DataFrame):
    cleaned_data = (
        data
        .pipe(change_column_names)
        .pipe(data_cleaning)
        .pipe(clean_lat_long)
        .pipe(calculate_haversine_distance)
        .pipe(create_distance_type)
        .drop(columns=columns_to_drop, errors='ignore')
    )
    return cleaned_data.dropna()

if __name__ == "__main__":
    DATA_PATH = "swiggy.csv"
    OUTPUT_PATH = "swiggy_cleaned.csv"
    
    print('Loading swiggy data...')
    df = pd.read_csv(DATA_PATH)
    
    print('Executing data cleaning pipeline...')
    cleaned_df = perform_data_cleaning(df)
    
    print('Saving cleaned data to CSV...')
    cleaned_df.to_csv(OUTPUT_PATH, index=False)
    
    print(f'Done! Cleaned data saved successfully as {OUTPUT_PATH}.')