import pandas
import plotly.express as px
import re
import requests

'''
iso_code
continent
location
date
total_cases
new_cases
total_deaths
new_deaths
total_cases_per_million
new_cases_per_million
total_deaths_per_million
new_deaths_per_million
total_tests
new_tests
total_tests_per_thousand
new_tests_per_thousand
new_tests_smoothed
new_tests_smoothed_per_thousand
tests_units
stringency_index
population
population_density
median_age
aged_65_older
aged_70_older
gdp_per_capita
extreme_poverty
cvd_death_rate
diabetes_prevalence
female_smokers
male_smokers
handwashing_facilities
hospital_beds_per_thousand
life_expectancy
'''
'''
def processDates(date):
    if re.match("^../../....", date):
        return date[6:10:1] + "/" + date[0:2:1] + "/" + date[3:5:1]
    elif re.match("^./../....", date):
        return date[5:9:1] + "/0" + date[0:1:1] + "/" + date[2:4:1];
    elif re.match("^././....", date):
        return date[4:8:1] + "/0" + date[0:1:1] + "/0" + date[2:3:1];
'''

def processDates(date):
    if re.match("^../../....", date):
        return (int(date[6:10:1])*10000) + (int(date[0:2:1])*100) + int(date[3:5:1])
    elif re.match("^./../....", date):
        return (int(date[5:9:1])*10000) + (int(date[0:1:1])*100) + int(date[2:4:1]);
    elif re.match("^././....", date):
        return (int(date[4:8:1])*10000) + (int(date[0:1:1])*100) + int(date[2:3:1]);

#Downloading data
def loadData():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    r = requests.get(url, allow_redirects=True)

    open("owid-covid-data.txt", 'wb').write(r.content)
    return pandas.read_csv('owid-covid-data.txt', sep=',')
    
df = loadData()
df['date'] = df['date'].astype(str)

populations = df[['location', 'population']]
populations = pandas.DataFrame.drop_duplicates(populations)
populations = populations.nlargest(25, 'population');

tempArr = df[df['location'] == "World"]['date'].array

l = []
for i in tempArr:
    l.append(i)

popArray = []
for i in populations['location'].array:
    popArray.append(i)

df = df[df['location'].isin(popArray)]
df = df[df['location'] != 'World']
#df = df[df['total_cases'] != 0]


fig = px.scatter(df, x='total_cases', y='new_cases', animation_frame='date', animation_group='location', category_orders={'date': l}, text='location', size='population', color='continent', log_x=True, log_y=True, range_x=[0.9, 10000000], range_y=[0.9, 1000000])
fig.show()

'''
for col in df:
    print(col)
    print(df[col].dtype)
'''

'''
fig = px.scatter(df, x='total_cases', y='new_cases',
                 animation_frame='date', animation_group='location',
                 size='population', color='continent', hover_name='location',
                 log_x=True, range_x=[0, 5000000], range_y=[0, 1000000])
'''

