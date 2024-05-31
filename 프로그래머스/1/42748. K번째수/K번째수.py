def solution(array, commands):
    answer = []
    slicing =[]
    
    for command in commands:
        i,j,k=command
        slicing = array[i-1:j]
        slicing.sort()
        answer.append(slicing[k-1])
    return answer