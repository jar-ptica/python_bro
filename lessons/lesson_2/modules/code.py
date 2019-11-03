import sys
import os


path = '/home/lunarseer/dev/projects/python_bro/lessons+'

try:
    output = os.listdir(path)
    print(output)
except OSError:
    print('Input path returned OSError')
except:
    print('unknown error')
finally:
    print('finished')


print(sys.version)
# print(os)
