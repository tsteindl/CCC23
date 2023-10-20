from parse import parse

if __name__ == '__main__':
    path = "in/level1/level1_1.in"
    out_path = "out/level1/level1_1_out"
    with open(path, 'r') as f:
        res = ""

        map, coords = parse(f.read())
        print(map)
        print(coords)
        for i, j in coords:
            res += (map[i][j]) + "\n"

        print(res)
        with open(out_path, 'w') as out_f:
            out_f.write(res)
