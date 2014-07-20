import sys
from math import *

cases = int(sys.stdin.readline())

for i in range(0, cases):
    number = int(sys.stdin.readline())
    if number % 2 == 0: # jesli liczba jest parzysta
        res1 = number/2
        print res1 **2
    else:
        res2 = number/2
        res3 = res2+1
        print res2*res3
        
        
    
