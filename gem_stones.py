import sys
import string


#cases = int(sys.stdin.readline())
dict_array = []
cases = int(sys.stdin.readline())
for i in range(0, cases):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    line = sys.stdin.readline().strip()
    for letter in line:
        d[letter]+=1
    dict_array.append(d)
#Now we have to process our dictionaries.
counter = 0
flag = False #flaga informujaca o przejsciu petli.
        
for letter in string.ascii_lowercase:
    for diction in dict_array:
        if diction[letter] == 0:
            flag = True
            break # wyjdzie z jednej petli for
            

    if flag == False:
        counter += 1
    if flag == True:
        flag = False
print counter

        
            
    
        
    
        


