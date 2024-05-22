def solution(genres, plays):
    answer = []
    total={}
    for genre, play in zip(genres,plays):
        if genre in total.keys():
            total[genre]+=play
        else:
            total[genre]=play
    
    total_sorted=sorted(total.items(), key=lambda x: -x[1])
    
    # (인덱스, 장르, 재생횟수)로 데이터 재구성
    index_genre_play = [(i,genre,play) for i,(genre,play) in enumerate(zip(genres,plays))]
    
    # 장르별로 재생횟수 내림차순 정렬
    index_genre_play_sorted={}
    for genre in total.keys():
        index_genre_play_sorted[genre]=sorted([item for item in index_genre_play if item[1]==genre], key=lambda x: -x[2])
        
    # 각 장르별 상위 두 곡의 인덱스를 결과에 추가
    for genre,_ in total_sorted:
        cnt=0
        for item in index_genre_play_sorted[genre]:
            if cnt<2:
                answer.append(item[0])
                cnt+=1
            else:
                break
    
    return answer