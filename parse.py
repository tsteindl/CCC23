def parse(input):
    lines = input.splitlines()
    map = []
    size = lines.pop()

    for i in range(size):
        line = lines.pop()
        row = []
        for j in range(size):
            row.insert(line[i])
        map.insert(row)

    N = lines.pop()
    coords = []
    for i in range(N):
        line = lines.pop()
        coords.insert([line[0], line[1]])
    return map, coords