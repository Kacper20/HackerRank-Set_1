#!/bin/python
def partition(ar):    
    number = ar[0] # partition number.
    list_less = []
    list_more = []
    for i in range(1, len(ar)):
        if ar[i] < number:
            list_less.append(ar[i])
        else:
            list_more.append(ar[i])
    list_less.append(number)
    for num in list_more:
        list_less.append(num)
    for num in list_less:
        print num,

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
