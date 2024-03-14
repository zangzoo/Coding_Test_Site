# 빨리 끝나는 심사대로 가서 심사 => 각 심사대는 1명씩만 -> 모든 사람 심사받는데 걸리는시간 최소
# 입국심사 기다리는 사람 n, 각 심사관이 한명 심사하는데 걸리는 시간 배열 times
# 모든 사람이 심사받는데 걸리는 시간 출력
# n, time의 범위는 각각 1,000,000,000, 심사관은 100,000

def solution(n, times):
    total_time = 0
    start=1
    end=max(times)*n
    while start<=end:
        mid=(start+end)//2
        people=0 
        for time in times:
            people += mid//time # 모든 심사관들이 mid분 동안 심사한 사람의 수
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people>=n:
                break
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if people>=n:
            total_time = mid
            end=mid-1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우    
        else:
            start=mid+1
    return total_time