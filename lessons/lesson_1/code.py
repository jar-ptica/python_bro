# cycle examples

"""
i = 0
for x in range(0, 10):
    print(i, x)
    i += 1


for i, x in enumerate(['sdfsd', 8646, 324]):
    print(i, '==', x)


i = 0
for elem in ['sdfsd', 8646, 324]:
    print(i, elem) 
    i += 1


active = True
i = 0

while active:
    print(i, '- Iterating')
    i += 1
    if i >= 15:
        active = False
"""

# Logic 

"""
def logic(a=None):
    if a:
        print('a is : ', a)
    elif a == 1:
        print('a equal 1')
    elif a == 2:
        print('a equal 2')
    else:
        print('a not given')

logic(4)
"""

lst = [10, 15, 'sdfs', 15.0, 12, True, None, -10, -5.4]

def check_list(lst):
    nlst = []
    for item in lst:
        try:
            nlst.append(int(item))
        except ValueError:
            print('Bad value', item)
        except TypeError:
            print('Bad Type', item)
        # except Exception as e:
        #     print(e)
        # except:
        #     raise KeyError
    return nlst
    

new_lst = check_list(lst)
print(new_lst)