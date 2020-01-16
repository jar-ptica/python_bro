bool_data = True
int_data = 120 #int type
float_data = 1.2099999 #float type
string_data = 'Some_data' #string type
list_data = ['some_data', 150, 1.2]
tuple_data = ('0','some_data', '1', 150)
dict_data = {'0': 'some_data', '1': 150}

# built-ins datatypes

new_data = str(int_data)
new_data = float(int_data)
new_data = int(float_data)
new_data = bool(0)
new_data = dict(one=1, two='sd', list=list_data)
new_data = tuple(list_data)

# 

new_data = abs(-12)
new_data = round(float_data, 7)
new_data = len(list_data)
new_data = sum([150, 1.2])
new_data = max((150, 1.2, -6))
new_data = min((150, 1.2, -6))

# print(new_data, type(new_data))

# dir(list_data)   #!!!!!!
# help(list_data)

# new_data = list_data.pop(0)
new_data = list_data.append('new_data')
new_data = list_data.remove('some_data')
# new_data = list_data.append(input('enter new data:'))
new_data = range(0, 15)
new_data = range(1, 15, 2)



# for x in range(0, 15):
#     print(x)

# for x in list_data:
#     print(x)

# for x in enumerate(list_data, 1):
#     print(x)

# for i, x in enumerate(list_data, 1):
#     print(i, x)

n = 0
while n <= 5:
    print(n)
    n += 1 