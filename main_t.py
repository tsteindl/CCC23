from parse import parse

if __name__ == '__main__':
    path = "in/level1/level1_1.in"
    with open(path, 'r') as f:
        map, coords = parse(f.read())
        print(map)
        print(coords)
