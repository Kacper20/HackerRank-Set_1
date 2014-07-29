from collections import defaultdict
len = int(raw_input())
numbers = map(int, raw_input().split())
d = defaultdict(int)
for number in numbers:
    d[str(number)] += 1

for key in d:
    if d[key] == 1:
        print int(key)
    
    