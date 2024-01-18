import requests

keyword = input('Enter the keyword: ').replace(' ', '+')

api = '12757425-e9abcdd5c3b62953dff94ca3d'
url = f'https://pixabay.com/api/?key={api}&q={keyword}&image_type=photo&pretty=true'

res = requests.get(url)
data = res.json()
page_url = data.get('hits')
image_id = 0
for image_url in page_url:
    single_image = image_url.get('webformatURL')
    response = requests.get(single_image)
    print(response.status_code)