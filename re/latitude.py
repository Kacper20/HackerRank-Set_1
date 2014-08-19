import re
for _ in range (input()):
    stri = raw_input()
    res = re.findall(r'\((.+),.?(.+)\)', stri)
    print res[0][0]
    print res[0][1]