#clean terminal before execute
import os
os.system('clear') # linux
# os.system('cls') # windows


string_data = 'Some_data' #string type
int_data = 120 #int type
float_data = 120.2 #float type
list_data = ['some_data', 150, 1.2]
tuple_data = ('0','some_data', '1', 150)
dict_data = {'0': 'some_data', '1': 150}

def multiple_return():
    value_a, value_b = 'ololo', 'OLOLO'
    return value_a, value_b


multiple_values = multiple_return() #['ololo', 'OLOLO']
value_a, value_b = multiple_return() #['ololo', 'OLOLO']

"""
 a = 10
 a += 1  >>  a = a + 1
 a -= 1  >>  a = a - 1
"""


def print_input_data(data='default value'): #single attribute
    print(data, type(data))

def print_input_data_mult_arg(data_b, data_a):  #positional arguments
    # print(data_a, data_b)
    print_input_data(data_a)
    print_input_data(data_b)

def print_input_data_with_named_argument(data='not valuable data', extra=''): #Named attributes
    print_input_data(data)
    print_input_data(extra)



# print_input_data('external_value')

# print_input_data_mult_arg(string_data, int_data)

# print_input_data_with_named_argument(data='not valuable data', extra='some_data')

# print_input_data_with_named_argument(
#     data=dict_data,
#     extra=list_data
#     )

# print_input_data(list_data[0]) # print item 1 from list_data 
# print_input_data(tuple_data[0]) # print item 1 from tuple_data 
# print_input_data(dict_data['1']) # item by key '1' from dict_data


# ================== String built-ins methods ==================

# path_parts = ['C:','Program Files', 'Autodesk', 'Maya2030'] #list
# new_string = 'C:' + '/' + 'Program Files' + '/' + 'Autodesk'
# new_string = '/' .join(path_parts) # joins list elements to string separates by main string value

new_string = 'Umbabarauma Ratamahata'
new_string = new_string.capitalize() # makes first symbol in Upper-case
new_string = new_string.lower() # makes all symbols in lower-case
# new_string = new_string.upper() # makes all symbols in Upper-case

# words_in_string = new_string.split('RA') #separates string to list by given character
# words_in_string = new_string.strip() #separates string to list by given character
# print(words_in_string, type(words_in_string))

# new_string = new_string.replace('a', 'u') # replace old value for new value

# = method cheat
#print(type(new_string))
#for method in dir(new_string):
#    print(method)

# print(new_string)

# ================== Logic operators ==================

"""
Comparison

is 

== equal
!= not equal
< less
> greater
<= less or equal
>= greater or equal

not a == b (a != b)

# logic ops

if
elif
else

"""
a = 1
b = 1
# print (1 == 1) #True
# print (not 1 == 1) #False
# print (1 is 1.0) #False


# print (a is b) #False

# print (1 == 2) #False
# print (1 != 1) #False
# print (1 <= 1.0) #True

# if a == b:
#     print('equal')
# else:
#     print('not equal')

text = 'french fries'
text = ''
lst = ['']

# if lst:
#     print(lst)
# else:
#     print('Empty List!!!')

# if 'fri' in text:
    # print ('found')


def absurd_example(value):
    if not value:
        print('no value!!!')
        return None
    else:
        if value < 0:
            return abs(value * 2)
        else:
            return value * 5


def another_absurd_example(value):
    if isinstance(value, int): # type checking
        result = ('is int')
    elif isinstance(value, float):
        result = ('is float')
    else:
        result = ('unknown type')
    return result
        

# print(absurd_example(0.005))
# print(another_absurd_example('sd'))

# ================== Erros Handling ==================

def error_function(data=None): #blocking error handling
    if not data:
        raise ValueError('Empty data comes!!! alarma!!!')
    elif not isinstance(data, list):
        raise TypeError('Wrong data type, need list!!!')
    else:
        return ' '.join(data)


def error_function_b(data=None): #non-blocking error handling(try/catch)
    try:
        return error_function(data)
    # except:
        # print('Kakaya to pizdec oshibka!!!!') # DO NOT DO THIS
        # return ''
    except Exception as e:
        print(e)
        return ''

    """
    except ValueError:
        blalsl
    """

test_data = ['rama', 'krishna', 'kali']
print(error_function_b(210))