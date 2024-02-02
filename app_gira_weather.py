import requests
import pandas as pd
import time

# libraries to open image
from PIL import Image
from io import BytesIO

def space1():
    print(                                                          )

def welcome_ironhack_game():
    # Carregar a imagem
    imagem = Image.open('phone 1.jpg')
    # Mostrar a imagem
    imagem.show()
    space1()
    print("Welcome to Gira Weather App.")
    space1()
    start_game()

def start_game():
    space1()
    question = input("Do you want to take a bike?   v1.1 (yes/no)")
    if question == "yes":
        space1()
        print("ok, let's go")
        space1()
        introdction()
    elif question == "no":
        print("ok, see you another day")
        exit
    else:
        print("sorry, I didn't understand that")

def introdction():
    print("You just woke up and discovered that you are in a bike station. Explore the App to find available bikes and weather.")
    examine_object()

def examine_object():
    url = 'https://opendata.emel.pt/cycling/gira/station/availability'
    response = requests.get(url)
    st_availability = response.json()
    station_id = input("Enter the ID of the bike station: ")
    station_data = next((station['properties'] for station in st_availability['features'] if station['properties']['id_expl'] == str(station_id)), None)
    space1()
    print(f"In Gira Station {station_id} there are {station_data['num_bicicletas']} bikes available")
    space1()
    show_weather_summary()
    
    
def show_weather_summary():     
    url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json"
    r = requests.get(url)
    df1 = r.json()
    df1 = df1["data"]
    real_time_data = pd.DataFrame(df1)
    lisbon_weather = real_time_data[real_time_data["globalIdLocal"] == 1110600].copy()  # Create a copy of the DataFrame
    
    # Convert temperature and precipitation probability to numeric types using .loc
    lisbon_weather.loc[:, "tMin"] = pd.to_numeric(lisbon_weather["tMin"])
    lisbon_weather.loc[:, "tMax"] = pd.to_numeric(lisbon_weather["tMax"])
    lisbon_weather.loc[:, "precipitaProb"] = pd.to_numeric(lisbon_weather["precipitaProb"])
    
    average_temp = (lisbon_weather["tMin"] + lisbon_weather["tMax"]) / 2
    rain = lisbon_weather["precipitaProb"].mean()  # Calculate the mean probability of raining
    print(f"The average temperature for today is {average_temp.iloc[0]:.2f}°C")
    space1()
    print(f"And today there's {rain:.2%} chance of raining")
    space1()
    print("Have a nice ride")
    time.sleep(3)
    imagem = Image.open('phone3.jpg')
    # Mostrar a imagem
    imagem.show()

# Start the game
welcome_ironhack_game()