#Imports
import pandas
import plotly.express as px
import re
import requests

#Main method of preprocessor
def execute():
    df = loadData()
    
    #Process columns
    df['date'] = df['date'].astype(str)

    return df


#Downloading data
def loadData():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    r = requests.get(url, allow_redirects=True)

    open("owid-covid-data.txt", 'wb').write(r.content)
    return pandas.read_csv('owid-covid-data.txt', sep=',')

#Extracting dates
def dates(df):
    tempArr = df[df['location'] == "World"]['date'].array
    l = []
    for i in tempArr:
        l.append(i)
    return l

def filterCountries(df):
    populations = df[['location', 'population']]
    populations = pandas.DataFrame.drop_duplicates(populations)
    populations = populations.nlargest(25, 'population');

    popArray = []
    for i in populations['location'].array:
        popArray.append(i)

    df = df[df['location'].isin(popArray)]
    df = df[df['location'] != 'World']

    return df
