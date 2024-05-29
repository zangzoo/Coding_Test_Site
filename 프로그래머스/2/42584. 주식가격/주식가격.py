def solution(prices):
    l=len(prices)
    answer = [0]*l
    
    for now in range(l-1):
        for other in range(now+1,l):
            if prices[now]>prices[other]:
                answer[now]+=1
                break
            else:
                answer[now]+=1
    answer[l-1]=0    
    return answer