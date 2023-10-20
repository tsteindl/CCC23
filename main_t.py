from parse import parse

def check_same_island(map, c1, c2):
    visited = []
    next_visit = []

    next_visit.append([map[c1[0] + 1][c1[1]], map[c1[0]][c1[1] + 1], map[c1[0] - 1][c1[1]], map[c1[0]][c1[1] - 1]])


if __name__ == '__main__':
    path = "in/level2/level2_1.in"
    out_path = "out/level2/level2_1.out"
    with open(path, 'r') as f:
        res = ""

        map, coords = parse(f.read())
        print(map)
        print(coords)
        for c1,c2 in coords:
            check_same_island(map, c1, c2)
        # for i, j in coords:
        #     res += (map[i][j]) + "\n"

        # print(res)
        # with open(out_path, 'w') as out_f:
        #     out_f.write(res)



