string_data = 'Some_data' #string type
int_data = 120 #int type
float_data = 120.2 #float type
list_data = ['some_data', 150, 1.2]
tuple_data = ('0','some_data', '1', 150)
dict_data = {'0': 'some_data', '1': 150}


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

print_input_data(list_data[0]) # print item 1 from list_data 
print_input_data(tuple_data[0]) # print item 1 from tuple_data 
print_input_data(dict_data['1']) # item by key '1' from dict_data
