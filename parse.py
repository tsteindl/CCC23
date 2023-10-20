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
        line = lines.pop(0).split(",")
        coords.append([int(line[0]), int(line[1])])
    return map, coords