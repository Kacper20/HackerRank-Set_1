
T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    wrapper = 0
    
    answer += A/B
    wrapper += answer
    while (wrapper/C1 != 0):
        bonus = wrapper / C1 # dostajemy bonusowe czekolady
        wrapper = wrapper %C1 #reszte kuponow zachowujemy
        wrapper+=bonus # dostajemy kupony za kolejne czekolady
        answer+=bonus
        
    
    print answer
