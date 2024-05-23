import math
def solution(progresses, speeds):
    answer = []
    day= math.ceil((100-progresses[0])/speeds[0])
    cnt=0
    for progress,speed in zip(progresses,speeds):
        if math.ceil((100-progress)/speed) <=day:
            cnt+=1
        else:
            day=math.ceil((100-progress)/speed)
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    return answer