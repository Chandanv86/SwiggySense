from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='This project is an End-to-End Machine Learning pipeline designed to predict Swiggy delivery time (in minutes) based on various factors like weather conditions, traffic levels, distance, and delivery partner's age/rating.',
    author='Chandan Vaishnav',
    license='MIT',
)
