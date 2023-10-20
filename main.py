import parse
import os

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def open_file(path):
    with open(path, 'r') as f:
        map, colist = parse.parse(f.read())
        return map, colist


def first_task():
    in_folder = 'in//level1/'
    out_folder = 'out//level1'

    file_list = ['level1_example.in','level1_1.in', 'level1_2.in', 'level1_3.in', 'level1_4.in', 'level1_5.in']
    file_example = 'in//level1//level1_example.in'
    print(os.path.exists(file_example))

    for file in file_list:
        print(os.path.join(in_folder, file))
        map, colist = open_file(os.path.join(in_folder, file))
        with open(os.path.join(out_folder, f'{file}.out'), 'w') as f:
            for (row, col) in colist:
                f.write(f'{map[row][col]}\n')


if __name__ == '__main__':
    first_task()

