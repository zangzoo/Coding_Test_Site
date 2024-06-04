from itertools import permutations
import math

def isDecimal(num):
    if(num <= 1):
        return False 
    #에라토스테네스의 체
    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0:
            return False    
    return True
    
def solution(numbers):
    
    li = list(numbers) #한 문자씩 list화
    allNums = set() # 중복값들은 제거
    for i in range(1, len(numbers)+1): #1개부터 len(numbers)개까지 permutations로 고르기
        permutationList = permutations(li, i) #list 되어있는 numbers를 permutations 진행해서 리스트에 넣어주기
        for perm in permutationList: #permutation되어있는 리스트 순회
            num = int(''.join(perm)) #해당 리스트 join해서 숫자로 만들어주고 int형으로 변환
            allNums.add(num) #미리 만들어놓은 리스트에 추가해주기

    
    count = 0
    for num in allNums:
        #print(num)
        if isDecimal(num):#소수면 count+1
            count+=1
            
    return count