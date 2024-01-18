import requests
import json

page_counter = {}
base_url = 'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages'
letters = 'a'
for letter in letters:
    urls = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages'
    res = requests.get(urls).json().get('page_count')
    data = f'"{letter}":{res}'
    page_counter[letter] = res
with open('urls.txt', 'w+') as file:
    for single_letter, total_pages in page_counter.items():
        for page_number in range(1, 4):  # actual code = for page_number in range(1,total_pages+1):
            url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{single_letter}/pages/{page_number}'
            file.write(url + '\n')
with open('urls.txt', 'r') as file:
    url_lists = file.readlines()
with open('company url.txt', 'w', encoding='utf-8') as file:
    for final_url in url_lists:
        url_text = requests.get(final_url.strip())
        for company_name in url_text.json():
            company_id = company_name.get('id')
            endpoints = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/entity/{company_id}'
            file.write(endpoints + '\n')

