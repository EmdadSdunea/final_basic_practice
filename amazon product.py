from amazon_paapi import AmazonApi

KEY = 'AKIAJLACON6OBIO7YVMQ'
SECRET = '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'
TAG = 'gearknows-20'
COUNTRY = 'US'
amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)
item = amazon.get_items('B01N5IB20Q')[0]
brand = item.item_info.by_line_info.brand.display_value # Item title
manufacturers = item.item_info.by_line_info.manufacturer.display_value
image = item.images.primary.medium.url
features = item.item_info.features.display_values
for data in features:
    print(data)
