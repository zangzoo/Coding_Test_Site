def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer=False
    for i in range(len(participant)-1):
        if participant[i]!=completion[i]:
            answer= participant[i]
            break
            
    if answer==False:
        answer=participant[-1]
    return answer
            