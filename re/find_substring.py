import re
data = []
for _ in range (input()):
    str = raw_input()
    data.append(str)
    
for _ in range (input()):
    word = raw_input().strip()
    sum = 0
    for str in data:
        result = re.findall(r'\b\w+is\w+\b', str)
        sum += len(result)
    print sum