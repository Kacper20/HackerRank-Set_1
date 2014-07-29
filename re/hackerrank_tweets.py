import re
sum = 0
for _ in range (input()):
    str = raw_input()
    if re.match(r'.*[hH][aA][cC][kK][eE][rR][rR][aA][nN][kK].*', str):
        sum += 1
print sum