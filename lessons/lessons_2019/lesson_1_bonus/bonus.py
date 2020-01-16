variable_int = 10
variable_float = 10.0
variable_bool = False
message = "GoodValue"
variable_str = """ten = 20 ten = 20 ten = 20 ten = 20
                ten = 20 ten = 20 ten = 20 ten = 20"""

variable_list = [variable_int,
                variable_float,
                variable_bool,
                0,      #False
                0.0,    #False
                '',
                [''],
                {},
                True, # = 1
                False # = 0
                ]

variable_dict = {
    "key1": variable_bool,
    "key2": variable_float,
    "key3": variable_int,
    "key4": 1586.2
    }

message = 'dat mesedz iz gud'  


def print_list(values_list, message='standart message'):
    for x in values_list:
        if x:   # -> bool
            print(message, x) 
        else:
            print('empty')
      
print_list(variable_list, message=message)
