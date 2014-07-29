cases = int(raw_input())
for _ in range(cases):
    point1 = map(int, raw_input().split())
    point2 = map(int, raw_input().split())
    point3 = map(int, raw_input().split())
    point4 = map(int, raw_input().split())
    p1p2 = []
    p1p3 = []
    p1p4 = []
    for i in range(3):
        p1p2.append(point2[i]-point1[i])
        p1p3.append(point3[i]-point1[i])
        p1p4.append(point4[i]-point1[i])
    det = 0
    det += p1p2[0] * p1p3[1] * p1p4[2]
    det += p1p3[0] * p1p4[1] * p1p2[2] 
    det += p1p4[0] * p1p2[1] * p1p3[2]
    det -= (p1p2[2] * p1p3[1] * p1p4[0])
    det -= (p1p3[2] * p1p4[1] * p1p2[0])
    det -= (p1p4[2] * p1p2[1] * p1p3[0])
    if det is not 0:
        print 'NO'
    else:
        print 'YES'
        