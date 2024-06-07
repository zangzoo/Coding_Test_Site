from itertools import product

def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        # li를 1개부터 5개까지 조합해서 순회 => [('A'), ('E'), ...,('U','U','U','U',U') ]
        for per in product(li,repeat = i):
            # answer 리스트에 합쳐서 담아주기 => [A, E, ..., UUUUU ]
            answer.append(''.join(per))
    # answer 리스트 정렬 => 작은것대로 정렬됨 => 각각의 인덱스+1이 결과값이 됨
    answer.sort()
    return answer.index(word)+1