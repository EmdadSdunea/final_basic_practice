import requests
# url = 'https://api.ipify.org?format=json'
r = requests.get('https://api.ipify.org?format=json')
# data = response.json()
# ip = data['ip']
# print(ip)

ip = (r.json()['ip'])
details_ip = f'http://ip-api.com/json/{ip}'
ip_info = requests.get(details_ip)
data = ip_info.json()
country = data['country']
countrycode = data['countryCode']
city = data['city']

description = f'Your ip addres is {ip}. Your country is {country} and country code is {countrycode}. The city you live is {city}'
print(description)