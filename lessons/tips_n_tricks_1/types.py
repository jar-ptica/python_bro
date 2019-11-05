#comment/uncomment - Ctrl+/

types_list = [
    True, 1, 1.5, 'TEXT'
]

def print_type_info(typedata=None):
    print(typedata, 'type: ', type(typedata))
    print("="*25)
    # print(dir(typedata))


# i = 0
# for item in types_list:
#     print(i, item)
#     i += 1  #i = i + 1


# for i, item in enumerate(types_list):
#     print(i, item)


for item in types_list:
    print_type_info(typedata=item)