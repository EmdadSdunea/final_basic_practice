import requests
import base64

wp_url = 'https://mytest.local/wp-json/wp/v2/media/'
wp_admin = 'admin'
wp_password = 'a56Y a8Gq KFUN mqpO UVJg cGay'
credentials = f'{wp_admin}:{wp_password}'
wp_token = base64.b64encode(credentials.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
#
file_path = open('images/new_mage_1.jpg', 'rb')
files = {'file': file_path}
res = requests.post(url=wp_url, files=files, headers=wp_headers, verify=False)
print(res.json())
