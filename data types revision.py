# age  =35
# age2 ='AB'
# total = age+age2
# print(total)
mobile_data = {'status': True,
               'data': [{'name': 'Xioami Note 5', 'price': '300 USD', 'made': 'China'},
                        {'name': 'Samsung Note 5', 'price': '200 USD', 'made': 'USA'},
                        {'name': 'iPhone 5', 'price': '180.5 USD', 'made': 'Japan'},
                        {'name': 'Pixel  5', 'price': '89.60 USD', 'made': 'Russia'},
                        {'name': 'Techno  5', 'price': '110 USD', 'made': 'UK'},
                        {'name': 'Huawei  5', 'price': '350 USD', 'made': 'Malaysia'}

                        ],
               'exchange_rate': 120.5
               }
current_exchange_rate = mobile_data['exchange_rate']
all_data = mobile_data['data']

for data in all_data:
    model = data.get('name')
    price = data.get('price')[:-3]
    made = data.get('made')
    usd_to_bdt = float(price) * current_exchange_rate
    print(f'{model} is made in {made}.The mobile price is {price}USD, which is {usd_to_bdt} BDT')