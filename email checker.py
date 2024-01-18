import requests
email = input('Enter your email: ')
url = f'https://api.mailcheck.ai/email/{email}'
response = requests.get(url)
print(response.status_code)