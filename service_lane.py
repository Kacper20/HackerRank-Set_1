
test_line = map(int, raw_input().split())
cases = test_line[1]
array_of_width = map(int, raw_input().split())
for _ in range (cases):
    min = 2000
    ran = map(int, raw_input().split())
    for i in range (ran[0], ran[1]+1):
        if array_of_width[i] < min:
            min = array_of_width[i]
    print min





