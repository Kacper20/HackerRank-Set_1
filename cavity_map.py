arr = []
for _ in range (input()):
    amm = []
    stra = raw_input().split()
    amm = [x for x in stra[0]]
    arr.append(amm)
for i in range(len(arr)):
    arr[i] = [int(num) for num in arr[i]]
print arr

for i in range (len(arr)):
    for j in range (len(arr[i])):
        