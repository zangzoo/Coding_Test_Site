from collections import deque

t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    q=deque(list(map(int,input().split())))
    
    cnt=0
    while len(q) > 0:
        if q[0] == max(q):
            q.popleft()
            if m == 0:  
                cnt += 1
                break
            else:
                cnt += 1
                m -= 1  
        else:
            q.append(q.popleft())
            if m == 0:
                m += len(q) - 1  
            else:
                m -= 1 
    print(cnt)