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

# Convertendo a coluna 'tripStartDate' para string no formato desejado
df_statistics['tripStartDate'] = df_statistics['tripStartDate'].dt.strftime('%Y-%m-%d')

# Salvando o DataFrame em um arquivo JSON
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







# WEATHER: HISTORICO
url = "https://api.ipma.pt/open-data/observation/climate/temperature-min/lisboa/mtnmn-1106-lisboa.csv"
df_historico = pd.read_csv(url)
df_historico.to_json('df_historico.json', orient='records', lines=True)






import pandas as pd

url = "https://api.ipma.pt/open-data/observation/climate/precipitation-total/lisboa/mrrto-1106-lisboa.csv"
df_pret = pd.read_csv(url)
df_pret = df_pret[['date','mean']]
df_pret.rename(columns={'mean':'mean_pret'}, inplace=True)
df_pret['date'] = pd.to_datetime(df_pret['date']) 
df_pret = df_pret.head(58)

# Utilizando o método strftime para formatar a coluna 'date' como string
df_pret['date_str'] = df_pret['date'].dt.strftime('%Y-%m-%d')

# Salvando o DataFrame resultante em um arquivo JSON
df_pret[['date_str', 'mean_pret']].to_json('df_perci_formatted.json', orient='records', lines=True)