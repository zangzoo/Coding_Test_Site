import heapq

def solution(jobs):
    answer = 0
    now = 0 #현재 시간
    i=0 # 처리 개수
    start=-1 # 마지막 완료 시간
    heap=[]
    
    while i < len(jobs): # 처리개수가 작업의 개수보다 작을때 실행 => 모두 실행하면 종료
        for job in jobs: # 작업들 순회
            if start < job[0] <=now: # 작업의 요청시점이 마지막 완료 시점보다 크고 현재 시간보다 작거나 같을때
                heapq.heappush(heap,[job[1],job[0]]) # 힙에 [작업의 소요시간, 작업 요청시간]순으로 담기
        if heap: # 힙이 비어있지 않으면 => 현재 작업 가능하면
            current = heapq.heappop(heap) #작업 소요시간 가장 작은 애 처리
            start = now #마지막 완료시간 = 현재
            now+=current[0] # 현재 시간에 작업 소요시간 더하기
            answer += now-current[1] # 현재 시간에서 작업 요청 시간 빼기 => 요청으로부터 처리 시간
            i+=1 # 처리한 작업 개수 +1
        else: # 힙이 비어있으면 => 현재 작업 가능한 거 없으면
            now+=1 # 시간 늘려주기
    return answer//len(jobs) # 답 구해주기