import requests
from pprint import pprint

API_Key= '4010ba45befc1979fbcf1417fb6480c8'
city=input("Enter a city:")
base_url="http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)