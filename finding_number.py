import sys
def find_position(array, number, size):
    for i in range(0, size):
        if array[i] == number:
            return i
        
    

v = input()
m = input()
ar = [int(i) for i in raw_input().strip().split()]

print find_position(ar, v, m)
