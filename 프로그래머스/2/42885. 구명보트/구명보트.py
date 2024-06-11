from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q=deque(people)
    
    while len(q)>=2:
        m=q.pop()
        answer+=1
        if q[0]+m<=limit:
            q.popleft()
    if len(q)==1:
        answer+=1
        
        
    return answer