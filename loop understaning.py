# fruits = ['mango','banana','apple', 'watermelon']
# # i = 1
# # while i<len(fruits):
# #     print(fruits[i])
# #     i +=1
#
# for fruit in fruits:
#
#     if fruit == 'apple':
#         continue
#     print(f'The name of fruits is {fruit}')
# else:
#     print('no fruits left')
#crate a function where if you input temp in Celcious you can check it farenheight\

# user_inputted_degree = input('Input your temperature Here(example 10F or 20C): ')
# unit = user_inputted_degree[-1].lower()
# degree = int(user_inputted_degree[:-1])
# # print(unit)
# # print(degree)
#
#
# celcious_to_farengeight = (degree*9/5)+32
# fahrenheit_to_celcious = (degree -32)*5/9

# if unit == "c":
#     print(f'The fahrenheit temperature is {celcious_to_farengeight}')
# elif unit == 'f':
#     print(f'The celcious temperature is {fahrenheit_to_celcious}')
# else:
#     print('data is not okay')

# def weather_calculator(user_inputted_degree):
#     if unit == 'c':
#         result = celcious_to_farengeight
#     elif unit == 'f':
#         result = fahrenheit_to_celcious
#     return f'The expected temperature is: {result}'
# temp= weather_calculator(user_inputted_degree)
# print(temp)

for a in range(1,201):
    print(f'This is the number {a}')
