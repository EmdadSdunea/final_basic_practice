# usd = 500
# exchange_rate = 110
# bdt = usd * exchange_rate
# print('500 USD is equal to', bdt, 'BDT')
# what is modulus ?
# first_number = 3
# last_number = 20
# print('The Modulus is:', last_number%first_number)

# What is floor division?
# first_number = 25
# last_number = 4
# print('The floor division is: ',first_number//last_number)# normally it could be decimal number
# total_member = 157
# seat_per_bus = 40
# total_bus_needed= total_member//seat_per_bus
# remaining_member = total_member%seat_per_bus
# print(total_bus_needed)
# print(remaining_member)
# number = int(input('Enter your number here: '))
# if number%2==0:
#     if number ==0:
#         print(number,'is zero')
#     else:
#         print(number, 'is even')
# else:
#     print(number, 'is odd')
number = int(input('Enter your Number: '))
if number >=80 and number <=100:
    print('A+')
elif number>=70 and number <=79:
    print('A')
elif 70 >= number >= 0:
    print('You have failed')
else:
    print('Invalid number')

