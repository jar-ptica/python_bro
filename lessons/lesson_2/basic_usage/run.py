import config
from second import get_dir_contents
from second import print_range


def main():
    print('running master script')
    print('User Name: ', config.USER_NAME)
    print('User Dir: ', config.USER_DIR)
    print('User Dir Children: ')
    for c in get_dir_contents(path=config.USER_DIR):
        print(c)

    # print_range()

main()