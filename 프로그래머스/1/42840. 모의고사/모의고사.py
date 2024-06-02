def solution(answers):
    answer = [0]*3  # 각 사람의 정답 수를 저장할 리스트
    result = []  # 최고 점수를 받은 사람을 저장할 리스트
    persons = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    for idx, person in enumerate(persons):
        # 패턴을 answers의 길이만큼 반복 확장
        repeated_pattern = (person * ((len(answers) // len(person)) + 1))[:len(answers)]
        
        # answers와 repeated_pattern 비교
        for a, p in zip(answers, repeated_pattern):
            if a == p:
                answer[idx] += 1

    max_score = max(answer)  # 최대 점수 찾기
    for i, score in enumerate(answer):
        if score == max_score:
            result.append(i + 1)  # 인덱스는 0부터 시작하므로 1 더해줌
    
    return result
