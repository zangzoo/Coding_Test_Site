import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>0:
        first=heapq.heappop(scoville)
        if first<K:
            if not scoville:
                return -1
            else:
                second=heapq.heappop(scoville)
                heapq.heappush(scoville,first+(second*2))
                answer+=1
        else:
            return answer