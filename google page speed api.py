import requests
api = 'AIzaSyB_xDruWV-_i_RUWMG0y9gihXSoEBtBz94'
sit_url = input('Enter your website URL: ')
url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={sit_url}/&key={api}'
website_info = requests.get(url)
print(website_info.json())