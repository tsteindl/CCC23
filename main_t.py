from parse import parse


def search(map, visited, next_v, goal):
    res = "DIFFERENT"
    while (len(next_v) > 0):
        c = next_v.pop(0)
        if c[0] >= len(map) or c[1] >= len(map[0]):
            continue
        if c in visited:
            continue
        if map[c[0]][c[1]] == "W":
            continue
        if c == goal:
            res = "SAME"
            break
        visited.append(c)
        next_v = [[c[0], c[1] + 1], [c[0] + 1,c[1]], [c[0] - 1, c[1]], [c[0], c[1] - 1]] + next_v
    return res + "\n"


def check_same_island(map, c1, c2):
    visited = []
    next_v = [c1]

    res = search(map, visited, next_v, c2)
    return res


if __name__ == '__main__':
    path = "in/level2/level2_1.in"
    out_path = "out/level2/level2_1.out"
    with open(path, 'r') as f:
        res = ""

        map, coords = parse(f.read())
        print(map)
        print(coords)
        for c1,c2 in coords:
            res += check_same_island(map, c1, c2)
        # for i, j in coords:
        #     res += (map[i][j]) + "\n"

        # print(res)
        with open(out_path, 'w') as out_f:
            out_f.write(res)



