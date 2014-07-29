import re
for _ in (input()):
    str = raw_input()
    matchip4 = re.search(r'(\d+)[.]{1}(\d+)[.]{1}(\d+)[.]{1}(\d+)', str)
    if matchip4:
        a = matchip4.group(1)
        b = matchip4.group(2)
        c = matchip4.group(3)
        d = matchip4.group(4)
        if a >= 0 and a <= 255 and b>= 0 and b<= 255 and c>= 0 and c <= 255 and d>= 0 and d<= 255:
            print 'IPv4'
            continue
    matchip6 = re.search(r'[]:[]:[]:', str)
    if matchip6:
        print 'IPv6'
        continue
    print 'Neither'