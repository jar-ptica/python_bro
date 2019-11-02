import sys
import os


path = '/home/lunarseer/dev/projects/python_bro/lessons+'

try:
    output = os.listdir(path)
    print(output)
except FileNotFoundError:
    print('Input path returned FileNotFoundError')
except:
    print('unknown error')
finally:
    print('finished')


# print(sys)
# print(os)
