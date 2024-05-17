def solution(citations):
    citations.sort(reverse=True)
    # H-지수를 계산하는 과정에서 각 논문이 인용된 횟수와 그 순서 중 더 작은 값을 고려하기 위함
    answer = max(map(min, enumerate(citations, start=1)))
    return answer