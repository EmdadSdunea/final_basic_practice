import requests
import base64

media_url = 'https://mytest.local/wp-json/wp/v2/media/'
post_url = 'https://mytest.local/wp-json/wp/v2/posts/'

wp_admin = 'admin'
wp_password = 'a56Y a8Gq KFUN mqpO UVJg cGay'
credentials = f'{wp_admin}:{wp_password}'
wp_token = base64.b64encode(credentials.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
#
file_path = open('images/new_mage_1.jpg', 'rb')
file = {'file': file_path}
res = requests.post(url=media_url, files=file, headers=wp_headers, verify=False)
media_id = res.json().get('id')

data = {
    'title': 'This is awesome title',
    'slug': 'This sis awesome slug',
    'content': 'This is awesome content',
    'status': 'draft',
    'featured_media': media_id
}
response = requests.post(post_url, verify=False, headers=wp_headers, json=data)
print(res.text)
