import re
searchText = '<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>'
match = re.findall(r'<a href="(.+)">.+>(\w+\s*\w+)', searchText, re.I)
print match[0]