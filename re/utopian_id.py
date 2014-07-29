import re
for _ in range (input()):
    str = raw_input()
    if re.match(r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}', str):
        print 'VALID'
    else:
        print 'INVALID'