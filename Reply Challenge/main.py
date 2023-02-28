import requests
from bs4 import BeautifulSoup as bs4
from selenium import webdriver


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('final_result.csv')
# print(final_result)
# final_result.plot(x='Country', y='Mean wealth', kind='line')
# plt.xlabel('Country')
# plt.ylabel('Mean Wealth')
# plt.title('Mean Wealth by Country')
# plt.show()


# plt.scatter(data['Adults'], data['Mean wealth'])
# plt.xlabel('Adults')
# plt.ylabel('Mean Wealth')
# plt.title('Mean Wealth Vs Adults')
# plt.show()



# read in your csv file
df = pd.read_csv('final_result.csv')

# sort the dataframe by adult population
# df = df.sort_values('Adults',ascending=False)
#
# # select the top 5 countries with highest adult population
# top_5_population = df.head(5)
#
# # create the bar chart
# top_5_population.plot(kind='bar', x='Country', y='Mean wealth', color='skyblue')
#
# # add the x and y labels
# plt.xlabel('Country')
# plt.ylabel('Mean Wealth')
#
# # show the chart
# plt.show()

# sort the dataframe by mean wealth
df = df.sort_values('Mean wealth',ascending=False)

# select the top 5 countries with highest mean wealth
top_5_mean_wealth = df.head(5)

# create the bar chart
top_5_mean_wealth.plot(kind='bar', x='Country', y='Mean wealth', color='skyblue')

# add the x and y labels
plt.xlabel('Country')
plt.ylabel('Mean Wealth')

# show the chart
plt.show()