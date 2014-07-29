cases = int(raw_input())
for i in range (cases):
    num_size = int(raw_input())
    found = False
    for i in range(num_size+1):
        if i % 5 == 0 and (num_size-i) % 3 == 0: # jesli spelnia wymagania
            found = True
            str5 = (num_size-i) * [5]
            str3 = i * [3]
            for s in str3:
                str5.append(s)
            s = ''.join(map(str, str5))
            print int(s)
            break
    if found == False:
        print -1
        