cases = int(raw_input())
for _ in range(cases):
    numbers = map(int, raw_input().split())
    point1 = [numbers[0], numbers[1]]
    point2 = [numbers[2], numbers[3]]
    vec = []
    for i in range(2):
        vec.append(point2[i] - point1[i])
    a = point2[0]+vec[0]
    b = point2[1]+vec[1]
    print a, b