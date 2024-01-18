from amazon_paapi import AmazonApi
import requests
import base64
from random import choice
import json
import openai

user = 'journal'
pythonapp = 'VHQB 0tqH Qy0t rRxj 132s KOGB'
url = 'https://ajournalismhub.com/wp-json/wp/v2'
token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}
amazon = AmazonApi('AKIAJEJLTSHB5UZDJ3PQ', 'kLb/hVaPG3n8uHcyka1T2obKiNZYPretgacFHXQ6', 'topreview0ec-20', 'US', throttling=4)
with open('openai_keywords.txt') as file:
    kwlist = file.readlines()
kwlist = [x.strip() for x in kwlist]
# print(url)
for k in kwlist:
    print(k)
    search_result = amazon.search_items(keywords= k, sort_by="Featured")
    #print(search_result)
    n = 1
    dicts = {}
    all_img = []
    for items in search_result.items:
        allcontent = []
        row_title = items.item_info.title.to_dict()
        title = row_title['display_value']
        try:
            row_description = items.item_info.features.to_dict()
        except:
            row_description = ""
        try:
            description = row_description['display_values']
        except:
            description = ''
        image = items.images.to_dict()
        img_url = image['primary']['large']['url']
        raw_link = items.detail_page_url
        allcontent.append(title)
        allcontent.append(description)
        allcontent.append(img_url)
        allcontent.append(raw_link)
        dicts[n] = allcontent

        all_img.append(img_url)
        # csv_row('abcd.csv', allcontent)
        n += 1
    # print(dicts)
    wp_title = choice(["What is the Best " + k.title() + " of 2022",
                       "10 Best " + k.title() + " in 2022 Review",
                       "Best " + k.title() + " in 2022 With Buying Guide",
                       "Best " + k.title() + " of 2022 - (Buyer Guide Added)",
                       "How to Choose The Best " + k.title() + " ",
                       "What Are the Best " + k.title() + " in 2022",
                       "Buyers Guide of Best " + k.title() + " in 2022",
                       "List of Best " + k.title() + " in 2022",
                       "Best " + k.title() + " Reviews Roundup",
                       "Check the Winning list of Best " + k.title() + " ",
                       "10 Best " + k.title() + " : Buyer Guide (2022)"])
    slug = 'Best ' + k
    status = 'draft'
    # product_1
    product_title_1 = '<h3>' + '01' + ' ' + str(dicts[1][0]) + '</h3>'
    product_image_link_1 = '<a href="' + dicts[1][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[1][2] + '"' 'alt="" class="aligncenter"/></a>'
    product_button_1 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[1][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    content = (dicts[1][1])
    try:
        c = '<p>' + content[0] + '</p>'
    except:
        c = ''
    try:
        c1 = '<p>' + content[1] + '</p>'
    except:
        c1 = ''
    try:
        c2 = '<p>' + content[2] + '</p>'
    except:
        c2 = ''
    try:
        c3 = '<p>' + content[3] + '</p>'
    except:
        c3 = ''
    try:
        c4 = '<p>' + content[4] + '</p>'
    except:
        c4 = ''
    a1 = c + ' ' + '\n' + c1 + ' ' + '\n' + c2 + ' ' + '\n' + c3 + '' + '\n' + c4  #######################
    openai.api_key = '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'
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n"+a1+"\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc1 = response['choices'][0]['text']
    #print(desc1)
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + a1 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features1 = response['choices'][0]['text']
    #print(p_features1)
    try:
        product_desc_1 = product_title_1 + product_image_link_1 +p_features1+ desc1 + product_button_1
    except:
        product_desc_1 = ''

    # product2
    product_title_2 = '<h3>' + '02' + ' ' + str(dicts[2][0]) + '</h3>'
    product_image_link_2 = '<a href="' + dicts[2][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[2][2] + '"' 'alt="" class="aligncenter"/></a>'
    product_button_2 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[2][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    content2 = (dicts[2][1])

    try:
        cb = '<p>' + content2[0] + '</p>'
    except:
        cb = ''
    try:
        cb1 = '<p>' + content2[1] + '</p>'
    except:
        cb1 = ''
    try:
        cb2 = '<p>' + content2[2] + '</p>'
    except:
        cb2 = ''
    try:
        cb3 = '<p>' + content2[3] + '</p>'
    except:
        cb3 = ''
    try:
        cb4 = '<p>' + content2[4] + '</p>'
    except:
        cb4 = ''
    b2 = cb + ' ' + '\n' + cb1 + ' ' + '\n' + cb2 + ' ' + '\n' + cb3 + '' + '\n' + cb4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + b2 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc2 = response['choices'][0]['text']
    #print(desc2)
    ######
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + b2 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features2 = response['choices'][0]['text']
    #print(p_features2)
    try:
        product_desc_2 = product_title_2 + product_image_link_2 +p_features2+ desc2 + product_button_2
    except:
        product_desc_2 = ''

    # #product3
    product_title_3 = '<h3>' + '03' + ' ' + str(dicts[3][0]) + '</h3>'
    product_image_link_3 = '<a href="' + dicts[3][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[3][2] + '"' 'alt="" class="aligncenter"/></a>'
    product_button_3 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[3][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    content3 = (dicts[3][1])

    try:
        cbc = '<p>' + content3[0] + '</p>'
    except:
        cbc = ''
    try:
        cbc1 = '<p>' + content3[1] + '</p>'
    except:
        cbc1 = ''
    try:
        cbc2 = '<p>' + content3[2] + '</p>'
    except:
        cbc2 = ''
    try:
        cbc3 = '<p>' + content3[3] + '</p>'
    except:
        cbc3 = ''
    try:
        cbc4 = '<p>' + content3[4] + '</p>'
    except:
        cbc4 = ''
    d3 = cbc + ' ' + '\n' + cbc1 + ' ' + '\n' + cbc2 + ' ' + '\n' + cbc3 + '' + '\n' + cbc4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + d3 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc3 = response['choices'][0]['text']
    #print(desc3)
    ######
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + d3 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features3 = response['choices'][0]['text']
    #print(p_features3)
    try:
        product_desc_3 = product_title_3 + product_image_link_3 +p_features3+ desc3 + product_button_3
    except:
        product_desc_3 = ''

    # product4
    product_title_4 = '<h3>' + '04' + ' ' + str(dicts[4][0]) + '</h3>'
    product_image_link_4 = '<a href="' + dicts[4][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[4][2] + '"' 'alt="" class="aligncenter"/></a>'
    product_button_4 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[4][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'

    content4 = (dicts[4][1])

    try:
        cba = '<p>' + content4[0] + '</p>'
    except:
        cba = ''
    try:
        cba1 = '<p>' + content4[1] + '</p>'
    except:
        cba1 = ''
    try:
        cba2 = '<p>' + content4[2] + '</p>'
    except:
        cba2 = ''
    try:
        cba3 = '<p>' + content4[3] + '</p>'
    except:
        cba3 = ''
    try:
        cba4 = '<p>' + content4[4] + '</p>'
    except:
        cba4 = ''
    e4 = cba + ' ' + '\n' + cba1 + ' ' + '\n' + cba2 + ' ' + '\n' + cba3 + '' + '\n' + cba4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + e4 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc4 = response['choices'][0]['text']
    #print(desc4)
    ###
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + e4 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features4 = response['choices'][0]['text']
    #print(p_features4)
    try:
        product_desc_4 = product_title_4 + product_image_link_4 +p_features4+ desc4 + product_button_4
    except:
        product_desc_4 = ''


    # product5
    product_title_5 = '<h3>' + '05' + ' ' + str(dicts[5][0]) + '</h3>'
    product_image_link_5 = '<a href="' + dicts[5][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[5][2] + '"' 'alt="" class="aligncenter"/></a>'
    product_button_5 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[5][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    content5 = (dicts[5][1])
    try:
        cbb = '<p>' + content5[0] + '</p>'
    except:
        cbb = ''
    try:
        cbb1 = '<p>' + content5[1] + '</p>'
    except:
        cbb1 = ''
    try:
        cbb2 = '<p>' + content5[2] + '</p>'
    except:
        cbb2 = ''
    try:
        cbb3 = '<p>' + content5[3] + '</p>'
    except:
        cbb3 = ''
    try:
        cbb4 = '<p>' + content5[4] + '</p>'
    except:
        cbb4 = ''
    f5 = cbb + ' ' + '\n' + cbb1 + ' ' + '\n' + cbb2 + ' ' + '\n' + cbb3 + '' + '\n' + cbb4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + f5 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc5 = response['choices'][0]['text']
    #print(desc5)
    ####
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + f5 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features5 = response['choices'][0]['text']
    #print(p_features5)
    try:
        product_desc_5 = product_title_5 + product_image_link_5 +p_features5+ desc5 + product_button_5
    except:
        product_desc_5 = ''

    # product6
    try:
        product_title_6 = '<h3>' + '06' + ' ' + str(dicts[6][0]) + '</h3>'
    except:
        product_title_6 = ''
    try:
        product_image_link_6 = '<a href="' + dicts[6][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[6][2] + '"' 'alt="" class="aligncenter"/></a>'
    except:
        product_image_link_6 =''
    try:
        product_button_6 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[6][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    except:
        product_button_6 =''
    try:
        content6 = (dicts[6][1])
    except:
        content6 =''

    try:
        cbbf = '<p>' + content6[0] + '</p>'
    except:
        cbbf = ''
    try:
        cbbf1 = '<p>' + content6[1] + '</p>'
    except:
        cbbf1 = ''
    try:
        cbbf2 = '<p>' + content6[2] + '</p>'
    except:
        cbbf2 = ''
    try:
        cbbf3 = '<p>' + content6[3] + '</p>'
    except:
        cbbf3 = ''
    try:
        cbbf4 = '<p>' + content6[4] + '</p>'
    except:
        cbbf4 = ''
    g6 = cbbf + ' ' + '\n' + cbbf1 + ' ' + '\n' + cbbf2 + ' ' + '\n' + cbbf3 + '' + '\n' + cbbf4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + g6 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc6 = response['choices'][0]['text']
    #print(desc6)
    ###
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + g6 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features6 = response['choices'][0]['text']
    #print(p_features6)
    product_desc_6 = product_title_6 + product_image_link_6 +p_features6+ desc6 + product_button_6
    # product7
    try:
        product_title_7 = '<h3>' + '07' + ' ' + str(dicts[7][0]) + '</h3>'
    except:
        product_title_7 =''
    try:
        product_image_link_7 = '<a href="' + dicts[7][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[7][2] + '"' 'alt="" class="aligncenter"/></a>'
    except:
        product_image_link_7 =''
    try:
        product_button_7 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[7][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    except:
        product_button_7 =''

    try:
        content7 = (dicts[7][1])
    except:
        content7 =''

    try:
        cbd = '<p>' + content7[0] + '</p>'
    except:
        cbd = ''
    try:
        cbd1 = '<p>' + content7[1] + '</p>'
    except:
        cbd1 = ''
    try:
        cbd2 = '<p>' + content7[2] + '</p>'
    except:
        cbd2 = ''
    try:
        cbd3 = '<p>' + content7[3] + '</p>'
    except:
        cbd3 = ''
    try:
        cbd4 = '<p>' + content7[4] + '</p>'
    except:
        cbd4 = ''
    h7 = cbd + ' ' + '\n' + cbd1 + ' ' + '\n' + cbd2 + ' ' + '\n' + cbd3 + '' + '\n' + cbd4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + h7 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc7 = response['choices'][0]['text']
    #print(desc7)
    ###
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + h7 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features7 = response['choices'][0]['text']
    #print(p_features7)
    product_desc_7 = product_title_7 + product_image_link_7 +p_features7+ desc7 + product_button_7

    # product8
    try:
        product_title_8 = '<h3>' + '08' + ' ' + str(dicts[8][0]) + '</h3>'
    except:
        product_title_8 = ''
    try:
        product_image_link_8 = '<a href="' + dicts[8][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[8][2] + '"' 'alt="" class="aligncenter"/></a>'
    except:
        product_image_link_8 = ''
    try:
        product_button_8 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[8][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    except:
        product_button_8 = ''

    try:
        content8 = (dicts[8][1])
    except:
        content8=''

    try:
        acbb = '<p>' + content8[0] + '</p>'
    except:
        acbb = ''
    try:
        acbb1 = '<p>' + content8[1] + '</p>'
    except:
        acbb1 = ''
    try:
        acbb2 = '<p>' + content8[2] + '</p>'
    except:
        acbb2 = ''
    try:
        acbb3 = '<p>' + content8[3] + '</p>'
    except:
        acbb3 = ''
    try:
        acbb4 = '<p>' + content8[4] + '</p>'
    except:
        acbb4 = ''
    i8 = acbb + ' ' + '\n' + acbb1 + ' ' + '\n' + acbb2 + ' ' + '\n' + acbb3 + '' + '\n' + acbb4  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + i8 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc8 = response['choices'][0]['text']
    #print(desc8)
    ####
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + i8 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features8 = response['choices'][0]['text']
    #print(p_features8)
    product_desc_8 = product_title_8 + product_image_link_8 +p_features8 +desc8 + product_button_8

    # product9
    try:
        product_title_9 = '<h3>' + '09' + ' ' + str(dicts[9][0]) + '</h3>'
    except:
        product_title_9 =''
    try:
        product_image_link_9 = '<a href="' + dicts[9][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                           dicts[9][2] + '"' 'alt="" class="aligncenter"/></a>'
    except:
        product_image_link_9 = ''
    try:
        product_button_9 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                       dicts[9][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    except:
        product_button_9 = ''

    try:
        content9 = (dicts[9][1])
    except:
        content9 = ''

    try:
        cbb_d = '<p>' + content5[0] + '</p>'
    except:
        cbb_d = ''
    try:
        cbb1_d = '<p>' + content5[1] + '</p>'
    except:
        cbb1_d = ''
    try:
        cbb2_d = '<p>' + content5[2] + '</p>'
    except:
        cbb2_d = ''
    try:
        cbb3_d = '<p>' + content5[3] + '</p>'
    except:
        cbb3_d = ''
    try:
        cbb4_d = '<p>' + content5[4] + '</p>'
    except:
        cbb4_d = ''
    j9 = cbb_d + ' ' + '\n' + cbb1_d + ' ' + '\n' + cbb2_d + ' ' + '\n' + cbb3_d + '' + '\n' + cbb4_d  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + j9 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc9 = response['choices'][0]['text']
    #print(desc9)
    ######
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + j9 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features9 = response['choices'][0]['text']
    #print(p_features9)
    product_desc_9 = product_title_9 + product_image_link_9 +p_features9 +desc9 + product_button_9
    # product10
    try:
        product_title_10 = '<h3>' + '10' + ' ' + str(dicts[10][0]) + '</h3>'
    except:
        product_title_10 = ''
    try:
        product_image_link_10 = '<a href="' + dicts[10][3] + '"' + 'target="_blank" rel="nofollow noopener"><img src="' + \
                            dicts[10][2] + '"' 'alt="" class="aligncenter"/></a>'
    except:
        product_image_link_10 = ''
    try:
        product_button_10 = '<p style="text-align: center;"><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                        dicts[10][3] + '"' + 'rel="nofollow"><strong>Check Price at Amazon</strong></a></p>'
    except:
        product_button_10 = ''

    try:
        content10 = (dicts[10][1])
    except:
        content10 = ''

    try:
        cbbm = '<p>' + content10[0] + '</p>'
    except:
        cbbm = ''
    try:
        cbb1m = '<p>' + content10[1] + '</p>'
    except:
        cbb1m = ''
    try:
        cbb2m = '<p>' + content10[2] + '</p>'
    except:
        cbb2m = ''
    try:
        cbb3m = '<p>' + content10[3] + '</p>'
    except:
        cbb3m = ''
    try:
        cbb4m = '<p>' + content10[4] + '</p>'
    except:
        cbb4m = ''
    k10 = cbbm + ' ' + '\n' + cbb1m + ' ' + '\n' + cbb2m + ' ' + '\n' + cbb3m + '' + '\n' + cbb4m  #######################
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write an introduction article and product details based on the following information\n\"\"\"\n" + k10 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    desc10 = response['choices'][0]['text']
    #print(desc10)
    ####
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt="Write the product features point by point based on the following information\n\"\"\"\n" + k10 + "\n\"\"\"\n\n",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    p_features10 = response['choices'][0]['text']
    #print(p_features10)
    product_desc_10 = product_title_10 + product_image_link_10 +p_features10+ desc10 + product_button_10
    ########################################################################################
    # intro_text = '<p>Are you tired of seeking the best' + ' ' + k + ' ' + 'but not being able to discover any? Given how many items there are now, it is understandable. Furthermore, with the advent of marketing strategies, finding the correct' + ' ' + k + ' ' + 'this year may be more difficult.</p><p>There is good news! We have already done the legwork for you. Our specialists were able to identify the best ones available after going through many different brands and a large number of products! They are as follows:</p>'
    first_heading = '<h2>' + '10 Best' + ' ' + k.title() + ' ' + 'Reviews</h2>'
    b_guide1 = '<h2>Buying Guide for' + ' ' + k.title() + '</h2>'

    comp_title = '<h2>Our Top 10 Editor Picks of' + ' ' + k.title() + '<h2>'
    try:
        product_comp_table = '<table style="font-family: Open Sans; font-size: 15px;border-collapse: collapse; border: 2px solid #000000; color: #000000; width: 100%;" border="2" cellspacing="3" cellpadding="3""> <thead> <tr style="background-color: #daf7a6;"> <th style="width: 10%;">Ranking</th> <th style="width: 60%;">Products Name</th> <th style="width: 20%;">Action</th> </tr> </thead> <tbody> <tr> <td>01</td> <td>' + \
                         dicts[1][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[1][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>02</td> <td>' + \
                         dicts[2][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[2][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>03</td> <td>' + \
                         dicts[3][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[3][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>04</td> <td>' + \
                         dicts[4][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[4][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>05</td> <td>' + \
                         dicts[5][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[5][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>06</td> <td>' + \
                         dicts[6][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[6][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>07</td> <td>' + \
                         dicts[7][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[7][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>08</td> <td>' + \
                         dicts[8][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[8][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>09</td> <td>' + \
                         dicts[9][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[9][3] + '"><strong>Check Price</strong></a></td> </tr> \n<tr> <td>10</td> <td>' + \
                         dicts[10][
                             0] + '</td> <td><a class="myButton" style="background-color: #ff0000; text-align: center; border-radius: 20px; border: 1px solid #18ab29; display: inline-block; cursor: pointer; color: #ffffff; padding: 10px 25px; text-decoration: none; text-shadow: 0px 1px 0px #e00909;" href="' + \
                         dicts[1][3] + '"><strong>Check Price</strong></a></td> </tr> </tbody> </table>'
    except:
        product_comp_table = ''
    first_heading = '<h2>' + '10 Best' + ' ' + k.title() + ' ' + 'Reviews</h2>'
    b_guide1 = '<h2>Buying Guide for' + ' ' + k.title() + '</h2>'
    def gpt3(bguide):
        openai.api_key = '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'
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=bguide,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        content = response['choices'][0]['text']
        # print(content)
        return response['choices'][0]['text']


    query = 'Write a detailed feature based buying guide for ' + k
    buying_guide = gpt3(query)
    #print(buying_guide)
    # total buying guide in one place
    buyer_guide = b_guide1+buying_guide
    #intro
    def gpt3(stext):
        openai.api_key = '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'
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=stext,
            temperature=0.7,
            max_tokens=120,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        content = response['choices'][0]['text']
        print(content)
        return response['choices'][0]['text']


    query = 'Write an introductory professional article why you should read our review before buying ' + k
    intro = gpt3(query)
    #print(intro)
    ##conclusion
    def gpt3(stext):
        openai.api_key = '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'
        response = openai.Completion.create(
            engine="text-curie-001",
            prompt=stext,
            temperature=0.7,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        content = response['choices'][0]['text']
        print(content)
        return response['choices'][0]['text']


    query = 'Write a conclusion article after reading all of our reviews before buying ' + k
    conclusion = gpt3(query)
    #print(conclusion)
    finalnot = "<h2>Final Note</h2>"


    post = {'title': wp_title,
            'slug': slug,
            'status': status,
            'content': intro+comp_title + product_comp_table + first_heading + product_desc_1 + product_desc_2 + product_desc_3 + product_desc_4 + product_desc_5 + product_desc_6 + product_desc_7 + product_desc_8 + product_desc_9 + product_desc_10+buyer_guide+finalnot+conclusion,
            'categories': '3',
            'author': '1',
            'format': 'standard',
            }
    r = requests.post(url + '/posts', headers=headers, json=post)
    print(r)
