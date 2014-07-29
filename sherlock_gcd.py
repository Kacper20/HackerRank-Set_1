def NWD(a, b):
    if b == 0:
        return a
    return NWD(b, a%b)

cases = int(raw_input())
for _ in range (cases):
    len = raw_input()
    numbers = map(int, raw_input().split())
    # Jeśli znajdziemy jakiekolwiek dwie liczby