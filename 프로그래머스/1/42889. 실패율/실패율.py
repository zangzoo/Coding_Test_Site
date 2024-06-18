def solution(N, stages):

    #실패율
    ratio = {} #sorting위해 dictionary로 선언  
    # 전체 플레이어 수 > 스테이지 지날수록 줄어든다
    allPlayer = len(stages) 

    for i in range(1,N+1):
        if allPlayer == 0: # 스테이지에 도달한 플레이어 수가 0명일 때 
            ratio[i] = 0
        else:
            ratio[i] = stages.count(i)/allPlayer
            allPlayer -= stages.count(i) # 현재 스테이지에 멈춘 숫자만큼 제외

    # value 기준으로 정렬 후 key 출력
    return sorted(ratio, key=lambda x : ratio[x],reverse=True)