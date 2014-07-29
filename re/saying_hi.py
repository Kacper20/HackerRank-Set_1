import re
for _ in range (input()):
    str = raw_input()
    if re.match(r'^[hH][iI]\s[a-cA-Ce-zE-Z].+', str):
        print str