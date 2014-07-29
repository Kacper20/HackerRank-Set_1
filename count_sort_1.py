numbers = raw_input()
d = dict.fromkeys(range(100), 0)
str = raw_input().split( )
str = map(int, str)
for number in str:
    d[number] +=1
for key in d:
    for i in range(d[key]):
        print key,
        
# Wersja do 2 zadania, obie podobne.