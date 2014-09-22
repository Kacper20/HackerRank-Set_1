import re


for _ in range (input()):
    searchText = raw_input()
    match_link = re.findall(r'<a href="(.+)">', searchText, re.I)
    match_text_field = re.findall(r'>([\w\s.]+)', searchText, re.I)
    if len(match_link) > 0 and len(match_text_field) > 0:
        print ("%s,%s" % (match_link[0], match_text_field[0]))
    