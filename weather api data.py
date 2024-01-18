import requests
api_key ='edf521d6ab29617374b655b890f88859'
city_name = input('Enter your city id: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
data = requests.get(url).json()
weather_temp = data['main']['temp']
print(weather_temp)