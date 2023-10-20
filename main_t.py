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


def find_route(map, start, end):
    res = []
    visited = []
    next_v = [start]

    while len(next) > 0:
        c = next_v.pop(0)
        if map[c[0], c[1]] == "L":
            continue
        if c[0] >= len(map) or c[1] >= len(map[0]):
            continue
        if c == end:
            return []
        next_v = [
            [c[0] + 1, c[1]], [c[0] + 1, c[1] + 1], [c[0], c[1] + 1], [c[0] - 1, c[1]], [c[0] - 1, c[1] - 1], [c[0], c[1] - 1], [c[0] + 1, c[1] - 1], [c[0] - 1, c[1] + 1],
        ] + next_v
        visited.append(c)


def get_diag(c):
    return [c[0] + 1, c[1] + 1], [c[0] - 1, c[1] - 1], [c[0] + 1, c[1] - 1], [c[0] - 1, c[1] + 1]

def get_adj(c):
    return [c[0] + 1, c[1]], [c[0] - 1, c[1]], [c[0], c[1] - 1], [c[0], c[1] + 1]
def check_route(map, route):
    res = "VALID"
    visited = []
    for c in route:
        for v in visited:
            if v == c:
                return "INVALID"
            # for d in get_diag(v):
            #     if d in visited:
            #         return "INVALID"
            # if [c[0] + 1, c[1]] in visited and [c[0], c[1] + 1] in visited or [c[0] + 1, c[1] + 1] in visited and [c[0], c[1] - 1] in visited or [c[0] + 1, c[1]] in visited and [c[0], c[1] + 1] in visited


        visited.append(c)
    return res




if __name__ == '__main__':
    path = "in/level4/level4_example.in"
    out_path = "out/level4/level4_example.out"
    with open(path, 'r') as f:
        res = ""
        map, coords = parse(f.read())
        print(map)
        print(coords)
        for route in coords:
            # res += check_route(map, route) + "\n"
            res += find_route(map, route[0], route[1]) + "\n"
        print(res)
        # for i, j in coords:
        #     res += (map[i][j]) + "\n"

        # print(res)
        with open(out_path, 'w') as out_f:
            out_f.write(res)



