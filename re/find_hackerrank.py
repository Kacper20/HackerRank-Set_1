import re
for _ in range (input()):
    str = raw_input()
    if re.match(r'^(?=(hackerrank)).*(hackerrank)$', str):
        print 0
    elif re.match(r'^hackerrank.+', str):
        print 1
    elif re.match(r'.+hackerrank$', str):
        print 2  
    else:
        print -1
# USE OF LOOKAROUNDS _IMPORTANT