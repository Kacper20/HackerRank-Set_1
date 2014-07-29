import re
for _ in range (input()):
    str = raw_input()
    match = re.search(r'[A-Z][A-Z][A-Z][A-Z][A-Z]\d\d\d\d[A-Z]', str)
    if match:
        print 'YES'
    else:
        print 'NO'