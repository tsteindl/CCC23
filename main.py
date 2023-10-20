def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def open_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        map = list()
        colist = list()
        return map, colist

def get_co(col, row, map):
    return map[row][col]


if __name__ == '__main__':
    print_hi('PyCharm')

