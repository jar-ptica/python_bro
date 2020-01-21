#clean terminal before execute
import os
os.system('clear') # linux
# os.system('cls') # windows

bool_data = True
int_data = 120 #int type (numeric)
float_data = 1.2099999 #float type (numeric)
string_data = 'Some_data' #string type (iterable)
list_data = ['some_data', 150, 1.2] #list type (iterable, many)
list_data = [15, -17, 0] #list type (iterable, many)
tuple_data = ('0','some_data', '1', 150) #tuple type (iterable, many)
dict_data = {'0': 'some_data', '1': 150} #dict type (iterable)

# built-ins datatypes

new_data = str(int_data) #convert to string
new_data = float(int_data) #convert to float
new_data = int(float_data) #convert to int
new_data = bool(0) #convert to boolean, return boolean
new_data = dict(one=1, two='sd', list=list_data) #return dictionary type
new_data = list([10, 15, -17, 'some data']) #return list type
new_data = tuple(list_data) #return tuple
# new_data = long(10) #return long type

# 

new_data = abs(-12)             #absolute value (numeric)
new_data = round(float_data, 7) #rounds value (numeric)
new_data = len(list_data) #returns count of items in many (numeric)
new_data = sum([150, 1.2]) #returns sum of all items in many (numeric)
new_data = max((150, 1.2, -6)) #returns greatest value from many (numeric)
new_data = min((150, 1.2, -6)) #returns lowest value from many (numeric)

# print(new_data, type(new_data))

# dir(list_data)   #!!!!!!
# help(list_data)

# new_data = list_data.pop(0)   #remove and return value[0] from list 
# new_data = list_data.append('new_data') #add value to list at end
# new_data = list_data.remove('some_data') #remove value[0] from list
# new_data = list_data.append(input('enter new data:')) 
# new_data = range(0, 15) #return generator with 15 numeric items from 0 to 14
# new_data = range(1, 15, 2) #return generator with 7 numeric items from 1 to 13 with step 2   [1,3,5,7,9,11,13]



### Cycle iterations

# for x in range(0, 15):
#     print(x)


# list_data = sorted(list_data, reverse=1):
# for x in list_data:
#     print(x, type(x))

# for x in enumerate(list_data, 1):
#     print(x) # tuple
#     print(x[0], x[1]) # tuple

# for x, y in enumerate(list_data, 0):
#     print(x, y)

# n = 0
# while n <= 5:
#     print(n)
#     n += 1
    # n = n + 1 