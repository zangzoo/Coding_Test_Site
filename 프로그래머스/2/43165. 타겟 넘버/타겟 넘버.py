from collections import deque

def solution(numbers, target):
    answer = 0
    q=deque()
    n=len(numbers)
    # 처음값 세팅
    q.append([numbers[0],0]) 
    q.append([-1*numbers[0],0])
    
    while q:
        now,idx=q.popleft()
        idx+=1
        if idx<n:
            q.append([now+numbers[idx], idx])
            q.append([now-numbers[idx],idx])
        else:
            if now==target:
                answer+=1
    return answer