import requests
from datetime import datetime
import json
def weather_info(city):
    MYKEY = '' # get your key from https://home.openweathermap.org/api_keys this link and poss it here


    URL = f'https://api.openweathermap.org/data/2.5/weather'

    PARAMETRS = {
        'q':city,
        'appid':MYKEY
    }
    KELVIN = 273.15
    res = requests.get(URL, params=PARAMETRS).json()
    timezone = res['timezone']
    weather = res['weather'][0]['main']
    temp = round(res['main']['temp']-KELVIN, 2)
    sunrise = datetime.utcfromtimestamp(res['sys']['sunrise'] + timezone).strftime('%H:%M:%S %D-%M-%Y')
    sunset = datetime.utcfromtimestamp(res['sys']['sunset'] + timezone).strftime('%H:%M:%S %D-%M-%Y')
    wind = res['wind']['speed']
    humidity = res['main']['humidity']

    print(f"""The city you entered: in 🏙{city.title()}
Weather: 🌤 {weather}
Temperature: 🌡 {temp}g/r
Sunrise time: 🌅 {sunrise} da
Sunset time: 🌇 {sunset} da
Wind speed: 💨 {wind}m/s
Humidity level: 💧 {humidity}%""")
    

while True:
    print(f"_____________________________________")
    city = input('Enter the name of the city: ')
    if city == 'stop':
        break
    try:
        weather_info(city)
    except KeyError:
        print(f"Can't find {city} city.Please try again!!!")
    except Exception as d:
        print(d.__class__)
    
