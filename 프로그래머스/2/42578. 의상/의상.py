def solution(clothes):
    answer = 1
    closet = {} # 담을 딕셔너리 생성, {종류: 이름} 으로 담기

    for name,kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]
        else:
            closet[kind] = [name]
    
    # closet의 키,밸류 순회 => value 가지고 계산
    for _,value in closet.items():
        answer *= (len(value)+1)
         
    return answer-1
