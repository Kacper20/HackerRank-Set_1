import re

def validate(str):
    matchip4 = re.search(r'(\d+)[.]{1}(\d+)[.]{1}(\d+)[.]{1}(\d+)', str)
    if matchip4:
        a = int(matchip4.group(1))
        b = int(matchip4.group(2))
        c = int(matchip4.group(3))
        d = int(matchip4.group(4))
        if a >= 0 and a <= 255 and b>= 0 and b<= 255 and c>= 0 and c <= 255 and d>= 0 and d<= 255:
            return 'IPv4'
    matchip6 = re.search(r'[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}', str)
    if matchip6:
        return 'IPv6'
    return 'Neither'
    
    
all = []
for _ in range (input()):
    all.append(raw_input())
for item in all:
    print validate(item)
    
    
