import sys
input=sys.stdin.readline

n,m=map(int,input().split())

if n==1:
    answer=1
elif n==2:
    answer=(m+1)//2
    if answer>=5:
        answer=4
elif m<7:
    answer=m
    if answer>=5:
        answer=4
elif n>=3 and m>=7:
    answer=m-2
print(answer)
        