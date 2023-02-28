import requests
from bs4 import BeautifulSoup as bs4
from selenium import webdriver


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ambil data dari url dan mencari setiap benua
url = "https://simple.wikipedia.org/wiki/List_of_countries_by_continents"
page = requests.get(url).text
soup = bs4(page,"lxml")
continents = soup.find_all('h2' > 'span', {"class":"mw-headline"})

# ambil setiap benua selain di exclude
exclude = ["Antarctica","References","Other websites"]
target_continents = [continent.text for continent in continents if continent.text not in exclude]

# Ambil data setiap negara
ol_html = soup.find_all('ol')
all_countries = [countries.find_all('li',{"class":None, "id":None}) for countries in ol_html]

countries_in_continents = []
for items in all_countries:
    countries = []
    if items:
        for country in items:
            countries = [country.find('a').text for country in items if country.find('a')]
        countries_in_continents.append(countries)

countries_continent_category_df = pd.DataFrame(
    zip(countries_in_continents, target_continents),columns=['Country','Continent']
)
# print(countries_continent_category_df)
countries_continent_category_df = countries_continent_category_df.explode(
    'Country'
).reset_index(drop=True)
print(countries_continent_category_df)

happines_page = requests.get("https://en.wikipedia.org/wiki/List_of_countries_by_wealth_per_adult")
happines_soup = bs4(happines_page.content,'lxml')

# Cari seluruh table yang ada di Wikipedia dengan class "wikitable"
countries_table = happines_soup.find_all('table',{'class':'wikitable'})
# print(countries_table)
countries_score = pd.read_html(str(countries_table))

# Ambil table ke 2
countries_score = countries_score[1]
countries_score = countries_score.rename(columns={"Location":"Country"})
countries_score['Country'] = countries_score['Country'].str.replace('*','')
countries_score['Country'] = countries_score['Country'].str.strip()
print(countries_score)
merge_df = pd.merge(countries_score,countries_continent_category_df,how="inner",on='Country')
print(merge_df)
# merge_df.to_csv('final_result.csv')