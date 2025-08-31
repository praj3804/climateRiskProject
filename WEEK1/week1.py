import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset
df = pd.read_csv("/workspaces/climateRiskProject/WEEK1/historical_weather_data.csv") 

# finding shape...
print(df.shape)

# basic idea of what datatypes and non null attributes
print(df.info())

#description
print(df.describe())

# First 5 rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

print(df.Temperature.min())
#the minimum temperature is -9.91743116251698

print(df.Temperature.max())
# the maximum temperature is 34.80196798453765

# Week 1 Project Conclusion:
# - The dataset contains 1095 rows and 7 columns.  
# - No major missing values were found / Missing values were identified and can be handled later.  
# - The temperature ranges from -9 to 34  
# - The dataset is now ready for further cleaning, preprocessing, and model building in upcoming weeks.



# Distribution of numerical columns
df.hist(figsize=(15,10), bins=30, edgecolor='black')
plt.suptitle("Distribution of Numerical Features", fontsize=16)
plt.show()


