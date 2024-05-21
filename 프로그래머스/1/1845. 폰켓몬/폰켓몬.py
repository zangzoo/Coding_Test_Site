def solution(nums):
    return min(len(nums)/2, len(set(nums)))

#     l=len(nums)
#     uni = len(set(nums))
    
#     if uni>=l/2 :
#         return l/2
#     else:
#         return uni