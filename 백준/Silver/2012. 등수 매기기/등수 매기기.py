import sys
input=sys.stdin.readline

n=int(input())
predict=[]
result=0

for _ in range(n):
    predict.append(int(input()))

predict.sort()

for i in range(n):
    if predict[i] != i+1:
        result+= abs(predict[i]-i-1)
print(result)
