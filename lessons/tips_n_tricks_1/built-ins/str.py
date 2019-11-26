string_value = 'SOME MEANING STRING VALUE'.lower()
list_value = list(string_value) # ['S', 'O'...]
tuple_value = tuple(string_value) # ('S', 'O'...)
# print(string_value*2)


# print(string_value[-2]) 
# print(list_value[-2])
# print(tuple_value[-2])


# SLICES
# print(string_value[0:4])# print(string_value[0:4:2]) 
# print(string_value[4:])
# print(string_value[-1])


#STRING METHODS
# print(string_value.replace(' ', '*-*'))
# print(string_value.capitalize())
# print(string_value.endswith('value'))
# print(string_value.startswith('some'))

alphabet = {}
for number in range(1, 27):
    # alphabet[number] = chr(number)
    alphabet.update({number: chr(number+96)})

# print(alphabet)

data = [0, 1, 3, 2, 6, 9]

# for i in range (0, len(data)):
#     # print(i, data[i])
#     for j in range(1, len(data) - i):
#         # print(j, data[j])
#         if data[j-1] > data[j]:
#             data[j - 1], data[j] = data[j], data[j - 1]

print(sorted(data))

import string

print({index + 1: letter for index, letter in enumerate(string.ascii_lowercase)})

return {id+1: chr(id+97) for id in range(0, 26)}