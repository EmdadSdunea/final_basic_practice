import base64
import requests

json_post_url = 'https://jsonplaceholder.typicode.com/posts'
posts = requests.get(json_post_url).json()

user_name = 'admin'
application_password = 'XjiC q3bw yd4k siJ4 jDxo yMw2'
wordpress_credential = f'{user_name}:{application_password}'
wp_token = base64.standard_b64encode(wordpress_credential.encode('utf-8'))
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}


def slugify(text):
    url_word = text.strip().replace(' ', '-')
    return url_word


for post in posts:
    endpoints = 'https://mytest.local//wp/v2/posts'
    data = {
        'title': post['title'],
        'content': post['body'],
        'slug': slugify(post['title']),
        'status': 'draft'
    }
    response = requests.post(endpoints, json=data, headers=wp_headers, verify= False)
    print(response)