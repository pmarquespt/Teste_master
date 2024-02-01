import requests
import pandas as pd

# API: STATISTICS USAGE:

url = 'https://opendata.emel.pt/cycling/gira/statistics/usage'

response = requests.get(url)

statistics = response.json()

df_statistics = pd.DataFrame(statistics)

# Sorting values by dates

df_statistics['tripStartDate'] = pd.to_datetime(df_statistics['tripStartDate']) 
df_statistics = df_statistics.sort_values(by='tripStartDate', ignore_index=True)
df_statistics['totalHoursPerDay'] = df_statistics['totalSecondsPerDay']/3600
df_statistics.to_json('df_statistics.json', orient='records', lines=True)

# API: BIKELANES: 

url = 'https://opendata.emel.pt/cycling/gira/bikelanes'

response = requests.get(url)

bikelanes = response.json()

df_bikelanes = pd.DataFrame(bikelanes)

df_bikelanes.to_json('df_bikelanes.json', orient='records', lines=True)

# API: WEATHER 

url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json"
response = requests.get(url)
weather_data = response.json()
weather_data = weather_data['data']
weather_df = pd.DataFrame(weather_data)
lisbon_weather = weather_df[weather_df["globalIdLocal"] == 1110600]
lisbon_weather['average_temp'] = (lisbon_weather["tMin"] + lisbon_weather["tMax"]) / 2
lisbon_weather.to_json('lisbon_weather.json', orient='records', lines=True)