from itertools import permutations

def solution(k, dungeons):
    l=len(dungeons)
    compare=0
    
    for perm in permutations(dungeons, l):
        k1=k
        answer = 0
        for need,spend in perm:
            if k1>=need:
                k1-=spend
                answer+=1
            else:
                continue
        compare=max(compare,answer)
    return compare