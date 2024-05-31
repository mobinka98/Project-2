#!/usr/bin/env python
# coding: utf-8

# # Project2

# In[1]:


import requests
import pandas as pd


# ###### Download the datase
# 
# 

# In[2]:


# pip install requests


# In[3]:


url = "https://corgis-edu.github.io/corgis/datasets/csv/weather/weather.csv"
response = requests.get(url)


# ###### Write data to a file 
# 
# 

# In[5]:


with open("weather_data.csv", "wb") as file:
    file.write(response.content)


# ###### Read data

# In[6]:


weather_df = pd.read_csv("weather_data.csv")


# In[7]:


weather_df


# ###### Display information about the DataFrame
# 
# 

# In[10]:


print("Information about the DataFrame:")
print(weather_df.info())
print()


# ###### Display summary statistics of the DataFrame
# 
# 

# In[11]:


print("Summary statistics of the DataFrame:")
print(weather_df.describe())


# ###### Calculate average 

# In[12]:


avg_temperature = weather_df['Data.Temperature.Avg Temp'].mean()
max_temperature = weather_df['Data.Temperature.Max Temp'].mean()
min_temperature = weather_df['Data.Temperature.Min Temp'].mean()
avg_wind_direction = weather_df['Data.Wind.Direction'].mean()
avg_wind_speed = weather_df['Data.Wind.Speed'].mean()


# In[13]:


print(f"Average Temperature: {avg_temperature}")
print(f"Average Max Temperature: {max_temperature}")
print(f"Average Min Temperature: {min_temperature}")
print(f"Average Wind Direction: {avg_wind_direction}")
print(f"Average Wind Speed: {avg_wind_speed}")

