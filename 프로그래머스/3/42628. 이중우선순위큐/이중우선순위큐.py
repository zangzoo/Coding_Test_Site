from heapq import heappush, heappop

def solution(operations):
    heap=[]
    max_heap=[]
    
    for operation in operations:
        order,num = operation.split()
        num=int(num)
        
        if order=='I':
            heappush(heap,num)
        if order=='D':
            if heap:
                if num==-1:
                    heappop(heap)
                else:
                    heap.sort()
                    heap.pop()
    
    heap.sort()
    if heap:
        answer=[heap[-1],heap[0]]
    else:
        answer=[0,0]
    return answer