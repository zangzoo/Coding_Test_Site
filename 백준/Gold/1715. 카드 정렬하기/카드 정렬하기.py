import heapq

n=int(input())

#힙에 초기 카드 묶음 모두 삽입
heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0

# 힙에 원소 1개 남을 때까지
while len(heap)!=1:
    # 가장 작은 카드 두개
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    # 카드 묶음 합쳐 다시 삽입
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap,sum_value)
    
print(result)