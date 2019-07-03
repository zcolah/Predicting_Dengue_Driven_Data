# Predicting Dengue 
Arsalan Ahmed, Zoshua Colah

**Driven Data Score:19.4543**

*Please see results folder to see all submission csvs*


Hi, welcome to our Modelling Dengue Repo. We are two undergraduate students at the University of Washington in an introductory ML class applying Machine Learning models to predict Dengue in San Juan & Iquitos as part of the Driven Data Challenge.


## Feature Generation

As part of feature generation we have introduced Rolling Averages. 
There can be a lot of fluctuation in our variables which can cause bias in our model. To help reduce the bias we have introduced Rolling Averages to help provide a better understanding of the overall current scenario.

We have added rolling average columns for all the climate variables and vegetation indexes.

A simple rolling average (also called a moving average, if you wanted to know) is the unweighted mean of the last n values. In simple words: An average of the last n values in a data set, applied row-by-row, so that you get a series of average

One year has 52 weeks on average. Initially we decided to take n as 52 because of this.

However after running a for loop to find the week with the least MOE and best fit, we found that n as 50 would be better. Hence n is 50.

Please refer to our data_prep.py and iterator files to learn more.

## Models Used & Scores

	- K Nearest Neighbors: 19.4543
	- XG Boost: 25.4856
	- Random Forest: 34.1394	
	- Decision Tree: 50.0385	

## Notebook Structure

Our notebook is extremely long due to the amount of EDA we did and the number of datasets we created and tested with various Machine Learning models. 

**To help you navigate the notebook better, we recommend taking a look at our Table of Contents:***

**1. Setup & Importing Data**
    
    1. Rolling Averages - New Features Added 

**2. San Juan**

    0. Data Preperation
    1. Understanding our Data
    2. Missing Values
    3. Exploratory Data Analysis
    4. Outlier Engineering
    
    
**3. Iquitos**
    
    0. Data Preperation
    1. Understanding our Data
    2. Missing Values
    3. Exploratory Data Analysis
    4. Outlier Engineering   
    
**4. Machine Learning Models**
    
    1. KNN
    2. XG Boost
    3. Random Forest
    4. Decision Tree
    
**5. Comparision**

## Best Model

Our best model is kept in a separate notebook as well for easy viewing.

Thank You.