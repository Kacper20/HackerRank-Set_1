import re
for _ in range (input()):
    str = raw_input()
    match = re.match(r'(\d\d?\d?)[-\s](\d\d?\d?)[-\s](\d\d\d\d\d?\d?\d?\d?\d?\d?)', str)
    print 'CountryCode='+match.group(1)+',LocalAreaCode='+match.group(2)+',Number='+match.group(3)