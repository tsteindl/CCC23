def parse(input):
    lines = input.splitlines()
    map = []
    size = int(lines.pop(0))

    for i in range(size):
        line = lines.pop(0)
        row = []
        for j in range(size):
            row.append(line[j])
        map.append(row)

    N = int(lines.pop(0))
    coords = []
    for i in range(N):
        line = lines.pop(0).split(" ")
        for coord in line:
            c1, c2 = coord.split(",")
            coords.append([
                [int(c1[1]), int(c1[0])],
            ])
    return map, coords