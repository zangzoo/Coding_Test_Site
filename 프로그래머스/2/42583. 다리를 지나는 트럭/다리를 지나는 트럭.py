#모든 트럭이 다리를 건너려면 최소 몇소가 걸리는지
#트럭이 최대 bridge_length대 
#weight 이하까지의 무게, 완전히 오르지 않으면 무게 무시

#1. bridge_length 만큼 큐 길이 생성
#2. truck_weights 돌면서 큐에 넣어주기
#3. 큐가 weight보다 작거나 같아야 넣을 수 있음
#4. 들어간 트럭은 bridge_length만큼 있기

from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights) 
    
    currentWeight = 0 # 현재 다리 위의 무게
    
    while len(truck_weights) > 0:
        time =time+1

        currentWeight = currentWeight - bridge.popleft()

        if currentWeight + truck_weights[0] <= weight: #현재 다리 위 무게에 올라갈 트럭의 무게 합이 한계보다 작거나 같으면
            currentWeight = currentWeight + truck_weights[0] #현재 다리 위 무게에 더해줌 => 트럭이 올라감
            bridge.append(truck_weights.popleft()) #다리위에 올려주기

        else: 
            bridge.append(0) 
            
    time += bridge_length # 다리 길이 더해주기 => 마지막 트럭이 건너는 시간?
    
    return time