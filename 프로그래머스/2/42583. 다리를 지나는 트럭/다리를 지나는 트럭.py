def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = []  # 다리를 건너는 트럭의 정보를 저장할 리스트, (트럭 무게, 진입 시간)
    bridge_weight = 0  # 현재 다리 위의 총 무게

    while truck_weights or bridge:
        time += 1  # 시간은 항상 1씩 증가

        # 다리를 완전히 건넌 트럭을 다리에서 제거
        if bridge and bridge[0][1] + bridge_length == time:
            bridge_weight -= bridge.pop(0)[0]

        # 다리에 새로운 트럭을 올릴 수 있는지 확인
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            # 다리의 현재 무게 + 새 트럭의 무게가 최대 하중을 넘지 않으면
            truck = truck_weights.pop(0)  # 대기 중인 트럭을 꺼내고
            bridge.append((truck, time))  # 다리에 트럭을 올림 (트럭 무게, 현재 시간)
            bridge_weight += truck  # 다리 위의 무게 증가

    return time
