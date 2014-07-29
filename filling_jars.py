n, m = [int(x) for x in raw_input().split()]
suma = 0

for _ in range(m):
    a, b, size = [int(x) for x in raw_input().split()]
    suma += (b-a+1) * size
    
print suma/ n