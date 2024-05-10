# 크기보다 토핑들의 종류에 관심, 조각크기와 토핑개수 신경 X, 각 조각에 동일한 가짓수의 토핑이 올라가면 공평한것!!
# 공평하게 자르는 방법의 수를 출력해라

from collections import Counter

def solution(topping):
    answer = 0
    # 변수 요소의 각 갯수를 센다
    # 우선 내가 모든 토핑을 가지고 있다
    me = Counter(topping)
    # 아직 토핑이 없다
    bro = {}
    
    # 순회하면서 토핑을 하나씩 동생한테도 나눠준다
    for i in range(len(topping)):
        if topping[i] in bro:
            bro[topping[i]] += 1
        else:
            bro[topping[i]] = 1
        
        me[topping[i]] -= 1
        
        if not me[topping[i]]:
            del(me[topping[i]])

        # 내가 가진 토핑의 갯수와 동생이 가진 갯수가 같으면
        # 1을 더한다
        if len(me) == len(bro):
            answer += 1

    return answer