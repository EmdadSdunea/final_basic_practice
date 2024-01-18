my_list = [1,2,3,4,]
try:
    print(my_list[4])
except IndexError:
    print('Index out of range')
    pass
print('all good')