from collections import deque

def solution(priorities, location):
    answer = 0
    q=deque()
    
    for i in range(len(priorities)):
        q.append((i,priorities[i]))
    
    while q:
        now_i,now_p=q.popleft()
        if any(now_p < other_p for _,other_p in q):
            q.append((now_i,now_p))
        else:
            answer+=1
            if now_i==location:
                return answer