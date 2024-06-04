from itertools import permutations

def solution(k, dungeons):
    compare=0
    
    for perm in permutations(dungeons, len(dungeons)):
        k1=k
        answer = 0
        for need,spend in perm:
            if k1>=need:
                k1-=spend
                answer+=1
        compare=max(compare,answer)
    return compare