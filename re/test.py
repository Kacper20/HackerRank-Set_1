import re
item = 'familiarize its eniosje familiarise oneself familiarise familiarize'
word = ['familiar']
result = re.findall(r'\b%s\w+(?:ze|se)\b' %word,  item)
print result