def solution(priorities, location):
    answer=0
    q= [(i,p) for i,p in enumerate(priorities)]
        
    while priorities:
        now=q.pop(0)
        if any(now[1]<p[1] for p in q):
            q.append(now)
        else:
            answer+=1
            if now[0] ==location:
                return answer