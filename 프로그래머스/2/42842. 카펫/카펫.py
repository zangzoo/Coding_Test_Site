def solution(brown, yellow):
    for x in range(1,yellow+1):
        if brown == ((x*2)+((yellow/x)*2)+4) :
            return [max(x,yellow/x)+2, min(x,yellow/x)+2]
