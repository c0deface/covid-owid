import preprocessor
import pandas
import plotly.express as px
import re
import requests

df = preprocessor.execute()
l = preprocessor.dates(df)

df = preprocessor.filterCountries(df)

fig = px.scatter(df, x='total_cases', y='new_cases',
                 animation_frame='date', animation_group='location',
                 category_orders={'date': l}, text='location',
                 size='population', color='continent',
                 log_x=True, log_y=True,
                 range_x=[0.9, 10000000], range_y=[0.9, 1000000])
fig.show()

