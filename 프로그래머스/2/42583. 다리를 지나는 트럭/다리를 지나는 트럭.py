#모든 트럭이 다리를 건너려면 최소 몇초가 걸리는지 return 
# 트럭이 최대 bridge_length 대가 올라갈 수 있음 , 다리는 weight 이하 무게만 견딤, 다리에 완전히 오르지않았으면 무게 무시
# 정해진 순으로 건넘
# 최단 시간 안에 다리를 건너게

# 선입선출 => 큐

from collections import deque

def solution(bridge_length, weight, truck_weights):
    b_q=deque([0]*bridge_length)
    w_q = deque(truck_weights)
    time=0 #걸린 시간
    w_a=0 #총 무게
    while len(b_q):
        time+=1
        w_a -=b_q[0]
        b_q.popleft()
        if w_q:
            if w_a+w_q[0] <=weight:
                w_a+=w_q[0]
                b_q.append(w_q.popleft())
            else:
                b_q.append(0)
                
    return time   