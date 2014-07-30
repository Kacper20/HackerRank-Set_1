import re
data = []
for _ in range (input()):
    str = raw_input()
    data.append(str)
for _ in range (input()):
    search = raw_input().strip()
    word = search[0:len(search)-3]
    sum = 0
    for item in data:
        result = re.findall(r'\b%s\w+(?:ze|se)\b' % word, item)
        sum += len(result)
    print sum