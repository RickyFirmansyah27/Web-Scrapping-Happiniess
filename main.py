import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs4
import util

print('Web Scrapping Tingkat Bahagia Negara')
dataset = util.Dataset()
print()
print('Daftar Faktor Kebahagiaan')
print('1. GDP per capita')
print('2. Social support')
print('3. Healthy life expectancy')
print('4. Freedom to make life choices')
print('5. Generosity')
print('6. Perceptions of corruption')


def happyscore():
  dataset = pd.read_csv('final_result.csv', index_col=2)
  ax = dataset['Score'].plot(kind='bar', figsize=(30,5), title="Happiness Score For Each Country")
  ax.set_ylabel("Happiness Score")
  plt.show()

def histscore():
  dataset = pd.read_csv('final_result.csv', index_col=2)
  plt.figure(figsize=(45,15))
  plt.title("Histogram of Number of Countries Within A Range of Happiness Score")
  plt.xlabel("Happiness Score")
  plt.ylabel("Number of Countries")
  plt.hist(dataset['Score'], bins=9)
  plt.show()


def faktor():
  heatmap_df = dataset.drop(['Overall rank','Country','Continent'], axis=1)
  ax = sns.heatmap(heatmap_df.corr(), annot=True, fmt='.2f', cmap='Blues')
  plt.show()
  
def corelasi(data):
   sns.lmplot(x=data, y='Score', data=dataset, fit_reg=False)
   plt.show()

def corelasiPerBenua(data):
    sns.lmplot(x=data, y='Score', data=dataset, fit_reg=False, hue='Continent')
    plt.show()
