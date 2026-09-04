SwiggySense
==============================

This project is an End-to-End Machine Learning pipeline designed to predict Swiggy delivery time (in minutes) based on various factors like weather conditions, traffic levels, distance, and delivery partner's age/rating.

## Data Source & Dataset Description

### Data Source
* The dataset used in this project is a publicly available food-delivery dataset that has circulated online under names such as `deliverytime.txt`.
* The dataset is commonly used in food-delivery time prediction projects and is publicly available through multiple online sources.
* It is also publicly distributed/reposted through Kaggle and other educational/data-science resources (Kaggle acts as a public hosting/republication source here, not the original creator).
* One publicly accessible source where the dataset was made available is the [Intelligenza Artificiale Italia article](https://www.intelligenzaartificialeitalia.net/post/prevedere-i-tempi-di-consegna-con-python-e-il-deep-learning).
* The exact original creator/provenance of the raw records could not be independently verified from the available public evidence.

### Dataset Description
The dataset contains approximately 45.6K food-delivery records and features such as:
* Delivery person information
* Restaurant and delivery-location coordinates
* Order date and time
* Weather conditions
* Road traffic density
* Vehicle condition
* Order type
* Vehicle type
* Multiple deliveries
* Festival indicator
* City category
* Actual delivery time (`Time_taken(min)`)

The dataset contains real-world-style inconsistencies/noise such as missing values, inconsistent categorical formatting, placeholder coordinates, and other imperfections, making it useful for a realistic ML preprocessing and prediction workflow.

### Why I Chose This Dataset
* It directly matches the problem of predicting food-delivery time.
* It contains a meaningful combination of temporal, geographic, operational, environmental, and rider-related features.
* It is sufficiently large for meaningful EDA, feature engineering, model training, and evaluation.
* It contains realistic data-quality issues, making the project more representative of an end-to-end machine-learning workflow rather than a perfectly clean toy dataset.
* It allows investigation of how traffic, weather, delivery load, vehicle condition, location, and order timing influence delivery duration.
* The dataset is publicly accessible, reproducible, and suitable for demonstrating the complete ML pipeline.

*Note: This project is a Swiggy-inspired food-delivery time prediction project, while the dataset’s direct Swiggy provenance is not independently verified.*
Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
