def solution(nums):

    l=len(nums)
    uni = len(set(nums))
    
    if uni>=l/2 :
        return l/2
    else:
        return uni
