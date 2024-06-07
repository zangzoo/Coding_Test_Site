def solution(number, k):
    answer = []

    # number 순회
    for i in number:
        # k가 0보다 크고 = 문자열을 더 제거해야하고
        # answer이 비어있지 않고
        # answer의 마지막 수가 i보다 작을때 
        # => 한자리 씩 비교하며 채워넣는거
        while k > 0 and answer and answer[-1] < i:
            # i보다 작으니까 answer에서 빼기
            answer.pop()
            # 제거하나 했으니까
            k -= 1
        # 큰 애들 추가해주기
        answer.append(i)

    return ''.join(answer[:len(answer) - k]) #출력해야하는 길이만큼 슬라이싱해서 합쳐서 출력