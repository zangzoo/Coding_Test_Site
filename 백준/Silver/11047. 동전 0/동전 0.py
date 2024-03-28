import sys
input=sys.stdin.readline

n,k=map(int,input().split())
v=[]
coin=0
for _ in range(n):
    v.append(int(input()))
v.sort(reverse=True) #내림차순

for i in v:
    if i<=k:
        coin+=k//i # 현재 가치의 개수
        k%=i #나머지
        if k<=0:
            break

print(coin)    