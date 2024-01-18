from requests import get
import csv
with open('company url.txt','r', encoding='utf-8') as file:
    urls = file.readlines()

with open('company data.csv', 'a+',newline='') as csvfile:
    fieldnames = ['company_name','company_logo_url','company_website','company_phone','company_address','company_social']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for url in urls:
        company_data = {}
        data = get(url.strip())
        res = data.json()
        company_data['company_name'] = res.get('name')
        company_data ['company_logo_url'] = res.get('logo_url')
        company_data['company_website'] = res.get('website_url')
        company_data['company_phone'] = res.get('phone_number')
        company_city = res.get('location').get('city')
        company_state = res.get('location').get('state')
        company_country = res.get('location').get('country')
        company_postal_code = res.get('location').get('postal_code')
        company_data['company_address'] = f'{company_city},{company_state},{company_country},{company_postal_code}'
        company_data['company_social'] = res.get('social_links').get('linkedin_url')
        writer.writerow(company_data)

