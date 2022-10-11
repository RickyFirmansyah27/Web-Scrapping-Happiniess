import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs4

def benua():
  continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
  continents_countries_soup = bs4(continents_page,"lxml")
  continents = continents_countries_soup.find_all('h2' > 'span', {"class":"mw-headline"})
  unwanted_words = ["Antarctica","References","Other websites"]
  target_continents = [continent.text for continent in continents if continent.text not in unwanted_words]
  return target_continents

def negara():
  continents_page = requests.get("https://simple.wikipedia.org/wiki/List_of_countries_by_continents").text
  continents_countries_soup = bs4(continents_page,"lxml")
  ol_html = continents_countries_soup.find_all('ol')
  all_countries = [countries.find_all('li',{"class": None, "id": None}) for countries in ol_html]
  all_countries
  countries_in_continents = []
  for items in all_countries:
      countries = []
      if items:
          for country in items:
              countries = [country.find('a').text for country in items if country.find('a')]
          countries_in_continents.append(countries)
  return countries_in_continents
 
def scrapingData():
  target_continents = benua()
  countries_in_continents = negara()
  countries_continent_category_df = pd.DataFrame(zip(countries_in_continents, target_continents), columns=['Country', 'Continent'])
  countries_continent_category_df
  countries_continent_category_df = countries_continent_category_df.explode('Country').reset_index(drop=True)
  print(countries_continent_category_df)
  return countries_continent_category_df


def score():
  countries_score_page = requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report#2020_report")
  countries_score_soup = bs4(countries_score_page.content,'lxml')
  countries_score_table = countries_score_soup.find('table', {'class':'wikitable'})
  countries_score_df = pd.read_html(str(countries_score_table))
  countries_score_df = countries_score_df[0]
  countries_score_df = countries_score_df.rename(columns={"Country or region":"Country"})
  return countries_score_df

def Dataset():
  countries_continent_category_df =  scrapingData()
  countries_score_df = score()
  merged_df = pd.merge(countries_score_df, countries_continent_category_df, how='inner', on='Country')
  merged_df.to_csv('final_result.csv')
  return merged_df




