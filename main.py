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

def search(row1, col1, row2, col2, map):
    vmap = []
    next_visit = []
    for i in range(len(map)):
        vmap.append([False for i in range(len(map))])

    next_visit = [(row1, col1)]


    while(len(next_visit) > 0):
        item = next_visit[0]
        next_visit.remove(item)
        (row, col) = item
        vmap[row][col] = True
        search_list = []

        if row > 0 and row < len(map) -1:
            if col > 0 and col < len(map) - 1:
                search_list.append((row - 1,col - 1))
                search_list.append((row - 1, col + 1))
                search_list.append((row + 1,col - 1))
                search_list.append((row + 1, col + 1))
            elif col == 0:
                search_list.append((row - 1, col + 1))
                search_list.append((row + 1, col + 1))
            else:
                search_list.append((row - 1, col - 1))
                search_list.append((row + 1, col - 1))
        elif row == 0:
            if col > 0 and col < len(map) - 1:
                search_list.append((row + 1,col - 1))
                search_list.append((row + 1, col + 1))
            elif col == 0:
                search_list.append((row + 1, col + 1))
            else:
                search_list.append((row + 1, col - 1))
        else:
            if col > 0 and col < len(map) - 1:
                search_list.append((row - 1,col - 1))
                search_list.append((row - 1, col + 1))
            elif col == 0:
                search_list.append((row - 1, col + 1))
            else:
                search_list.append((row - 1, col - 1))

        for (row_c, col_c) in search_list:
            if map[row_c][col_c] == 'L':
                if row_c == row2 and col_c == col2:
                    return True
                else:
                    if not vmap[row_c][col_c]:
                        next_visit.append((row_c, col_c))

    return False








def second_task():
    in_folder = 'in//level2/'
    out_folder = 'out//level2'

    file_list = ['level2_example.in','level2_1.in', 'level2_2.in', 'level2_3.in', 'level2_4.in', 'level2_5.in']
    file_example = 'in//level2//level2_example.in'
    print(os.path.exists(file_example))

    for file in file_list:
        print(os.path.join(in_folder, file))
        map, colist = open_file(os.path.join(in_folder, file))
        with open(os.path.join(out_folder, f'{file}.out'), 'w') as f:
            for ((row1, col1), (row2, col2)) in colist:
                if search(row1, col1, row2, col2, map):
                    f.write('SAME\n')
                else:
                    f.write('DIFFERENT\n')




if __name__ == '__main__':
    second_task()

