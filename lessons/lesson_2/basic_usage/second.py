from os import listdir

def get_dir_contents(path=''):
    children = []
    for item in listdir(path):
        children.append(path + '/' + item)
    return children



def print_range():
    for x in range(1, 5):
        print(str(x))