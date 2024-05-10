# 크기보다 토핑들의 종류에 관심, 조각크기와 토핑개수 신경 X, 각 조각에 동일한 가짓수의 토핑이 올라가면 공평한것!!
# 공평하게 자르는 방법의 수를 출력해라

def solution(topping):
    answer = 0
    # 철수 케이크
    bro1 = {}
    for t in topping:
        if t in bro1:
            bro1[t] += 1
        else:
            bro1[t] = 1

    #동생 케이크
    bro2 = {}
    for t in topping:
        # 둘의 딕셔너리 크기가 같다면 동일한 크기로 나눈거
        if len(bro2) == len(bro1):
            answer += 1
        # 동생 케이크에 해당 토핑이 없다면 토핑 추가
        if t not in bro2:
            bro2[t] = 1
        
        # 철수 토핑에는 하나 빼주기
        bro1[t] -= 1
        # 만약 철수가 해당 토핑을 아예 가지고 있지 않다면 제거
        if bro1[t] == 0:
            del bro1[t]
        
    return answer
