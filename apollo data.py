from requests import get
letters = ['a','b','c','d','e','f','g',]
i = 1
for letter in letters:
    url = f'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/{letter}/pages'
    while i <=5000:
        new_url = f'{url}/{i}'
        i  +=1
        res = get(new_url)
        if res.status_code == 200:
            print(i,res.json()[0]['name'])

