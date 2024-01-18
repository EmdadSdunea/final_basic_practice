import requests
api = '12757425-e9abcdd5c3b62953dff94ca3d'
keywords = input('Enter the keyword: ').replace(' ', '+')

url = f'https://pixabay.com/api/?key={api}&q={keywords}&image_type=photo&pretty=true'
var = requests.get(url)
data = var.json()
all_images = data.get('hits')

image_id = 0
for single_image in all_images:
    new_url = single_image.get('webformatURL')
    res = requests.get(new_url)
    if res.status_code == 200:
        with open(f'images/new_mage_{image_id}.jpg', 'wb') as file:
            file.write(res.content)
    image_id += 1
