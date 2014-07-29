size = int(raw_input())
arr = raw_input().split( )
arr = map(int, arr)
incorr_var = arr[size-1];
i = size-2;
while incorr_var <= arr[i] and i>-1:
    arr[i+1] = arr[i]
    for num in arr:
        print num,
    print 
    i -=1
arr[i+1] = incorr_var
for num in arr:
    print num,
