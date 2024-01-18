from requests import get, post
import base64
import json

wp_user = 'admin'
wp_pass = 'uvKq nV0u BnMo icfk bDwf n1yY'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
wp_site_url = 'https://mytest.local/wp-json/wp/v2/posts/'

server_url = 'https://mobile-phone-server.vercel.app/phones'
res = get(server_url)
if res.status_code == 200:
    phones = res.json()['RECORDS']


def wp_paragrph(text):
    """

    :param text: this function will generate guttenbarg paragraph
    :return:
    """
    return f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'


def wp_heading_two(heading2):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{heading2}</h2><!-- /wp:heading -->'


def wp_heading3(heading3):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{heading3}</h2><!-- /wp:heading -->'


def slugify(text):
    slug_text = text.strip().replace(' ', '-')
    return slug_text


def wp_table(dictionary):
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}e </td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes


def image_rom_url(src, phone_Name):
    code = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --> <figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{phone_name}"/></figure> <!-- /wp:image -->'
    return code


for phone in phones:
    phone_name = phone.get('name')

    title = f'{phone_name} Price in Bangladesh'

    phone_price = phone.get('price')
    phone_ram = phone.get('ram')
    phone_rom = phone.get('storage')
    phone_specification_str = phone.get('specifications')
    # phone_specification = json.loads(phone_specification_str)
    # phone_color_str = phone.get('specifications')
    # phone_color = json.loads(phone_color_str)['Colors']
    # phone_brand_id = phone.get('brand_id')
    # network_type_data = json.loads(phone_color_str)['Technology']
    # network_2G = json.loads(phone_color_str)['2G bands']
    # #network_3G = json.loads(phone_color_str)['3G bands']
    # network_4G = json.loads(phone_color_str)['4G bands']
    # network_speed = json.loads(phone_color_str)['Speed']
    # # phone_price = json.loads(phone_color_str)['Price']
    # # network_gprs = json.loads(phone_color_str)['GPRS']
    # # network_edge = json.loads(phone_color_str)['EDGE']
    # image_url = phone.get('picture')
    #
    # phone_type = phone.get('os')
    #
    # paragraph = f'{phone_name} price starts from BDT. {phone_price}. {phone_name} internal storage base variant of {phone_ram} Ram, {phone_rom} Internal Memory (ROM). {phone_name} which is available in {phone_color} colour.'
    #
    # first_heading_two = f'{phone_name} Full  Specification'
    # first_heading = f'{phone_name} Network Data '
    # final_heading = f'{phone_name} Technical Details'
    #
    # first_table_dict = {
    #
    #     'Name': phone_name,
    #     'Brand Id': phone_brand_id,
    #     'Price': phone_price,
    #     'Phone Type': phone_type,
    #     'Ram': phone_ram,
    #     'Rom': phone_rom
    # }
    #
    # second_table_dict = {
    #     'Network Type': network_type_data,
    #     'Network 2G': network_2G,
    #     #'Network 3G': network_3G,
    #     'Network 4G': network_4G,
    #     'Speed': network_speed
    #     ,
    # }
    #
    # content = image_rom_url(image_url, phone_name) + wp_paragrph(paragraph) + wp_heading_two(first_heading_two) + wp_table(
    #     first_table_dict) + wp_heading_two(first_heading) + wp_table(second_table_dict) + wp_heading_two(
    #     final_heading) + wp_paragrph(phone_specification)
    #
    # data = {
    #     'title': title,
    #     'slug': slugify(title),
    #     'content': content,
    #     'status': 'publish',
    #     'format': 'standard'
    # }
    # r = post(wp_site_url, headers=wp_headers, json=data, verify=False)
    # #print(r)


phone_specification_str = phone.get('specifications')['Network']

