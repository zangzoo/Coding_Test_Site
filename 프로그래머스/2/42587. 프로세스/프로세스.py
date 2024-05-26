def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    while priorities:
        now=queue.pop(0)
        if any(now[1]<q[1] for q in queue):
            queue.append(now)
        else:
            answer+=1
            if now[0]==location:
                return answer