#comment/uncomment - Ctrl+/

types_list = [
    True, 1, 1.5, 'TEXT'
]

print(types_list[0])

i = 0
for item in types_list:
    print(i, item)
    i += 1

for i, item in enumerate(types_list):
    print(i, item)

def print_type_info(typedata=None):
    print(typedata, 'type: ', type(typedata))

for item in types_list:
    print_type_info(typedata=item)