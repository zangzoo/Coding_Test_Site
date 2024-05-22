def solution(genres, plays):
    answer = []
    total={}
    # total = {장르: 재생횟수}꼴로 만들기
    for genre,play in zip(genres,plays):
        if genre in total.keys():
            total[genre]+=play
        else:
            total[genre]=play
    
    total_sorted=sorted(total.items(),key=lambda x: -x[1])
    
    # (인덱스, 장르, 재생횟수) 형태로 데이터 재구성
    genre_play_list = [(i, genre, play) for i, (genre, play) in enumerate(zip(genres, plays))]
    
    # 장르별로 곡을 재생횟수 내림차순으로 정렬
    genre_play_sorted = {}
    for genre in total.keys():
        genre_play_sorted[genre] = sorted(
            [item for item in genre_play_list if item[1] == genre], key=lambda x: -x[2])

    # 각 장르별 상위 2곡의 인덱스를 결과에 추가
    for genre, _ in total_sorted:
        count = 0
        for item in genre_play_sorted[genre]:
            if count < 2:
                answer.append(item[0])
                count += 1
            else:
                break

    return answer                