# from requests import get
# url = 'https://texasaz.com/wp-json/wp/v2/users'
# r = get(url).json()
# data = r
# for info in data:
#     author_name = info.get('name')
#     link = info.get('link')
#     print(author_name,link)

data = ['apple','banana','orange','lemon', 'grape']
new_data = []
for x in data:
    new_data.append(x)
print(new_data)
