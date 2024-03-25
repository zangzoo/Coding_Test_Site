import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))
p.sort()
sum_t=0

for i in range(n):
    for j in range(1,i+2):
        sum_t+=p[j-1]
print(sum_t)