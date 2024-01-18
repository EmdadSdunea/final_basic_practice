from amazon_paapi import AmazonApi
import requests
import base64

wp_url = 'https://mytest.local/wp-json/wp/v2/posts'
user_name = 'admin'
application_password = '2xq6 Cgtz QYgT 8VC3 BNVE guYG'
wordpress_credential = f'{user_name}:{application_password}'
wp_token = base64.standard_b64encode(wordpress_credential.encode('utf-8'))
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

KEY = 'AKIAJLACON6OBIO7YVMQ'
SECRET = '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'
TAG = 'gearknows-20'
COUNTRY = 'US'
amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)


def wp_post(wp_url, data):
    res = requests.post(wp_url, json=data, headers=wp_headers, verify=False)
    print(res.status_code)


def wp_h2(text):
    code = f'<!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'
    return code


def wp_image(image_url):
    codes = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{image_url}" alt=""/></figure><!-- /wp:image -->'
    return codes


def wp_list(anylist):
    table_list = '<!-- wp:list --><ul>'
    for list_item in anylist:
        table_list += f'<!-- wp:list-item --><li>{list_item}</li><!-- /wp:list-item -->'
    table_list += '</ul><!-- /wp:list -->'
    return table_list


search_result = amazon.search_items(keywords='mobile')
content = ''
for item in search_result.items:
    title = item.item_info.title.display_value
    wp_title = wp_h2(item.item_info.title.display_value)  # Item color
    image = wp_image(item.images.primary.large.url)
    features = wp_list(item.item_info.features.display_values)
    content = wp_title + image + features
data = {
    'title': title,
    'slug': title,
    'content': content,
    'status': 'publish'
}
wp_post(wp_url, data)
