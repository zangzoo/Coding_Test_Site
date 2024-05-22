def solution(genres, plays):
    answer = []

    dic1 = {} #장르별 각 곡들의 인덱스, 재생횟수 담기
    dic2 = {} #장르별 총 재생횟수 담기

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in dic1:
            dic1[g].append((i,p))
        else:
            dic1[g]=[(i,p)]

        if g in dic2:
            dic2[g]+=p
        else:
            dic2[g] =p

    for (k, v) in sorted(dic2.items(), key=lambda x:-x[1]):
        for (i, p) in sorted(dic1[k], key=lambda x:-x[1])[:2]:
            answer.append(i)

    return answer

