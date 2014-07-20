from math import sqrt
import sys
def isFibonacci(n):
    if isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4):
        print "IsFibo"
    else:
        print "IsNotFibo"
def isPerfectSquare(n):
    r = sqrt(n)
    if r%1 == 0:
        return True
    else:
        return False
       

cases = int(sys.stdin.readline())
for m in range (0,cases):
    isFibonacci(int(sys.stdin.readline()))

    #Sprytny algorytmy - sprawdzamy czy liczba jest fibonacciego
    # http://en.wikipedia.org/wiki/Fibonacci_number#Recognizing_Fibonacci_numbers
        
