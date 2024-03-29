import sys
input=sys.stdin.readline

n,m=map(int,input().split())

if n==1:
    print(1)
elif n==2:
    print(min(4,(m+1)//2))
elif m<7:
    print(min(4,m))
elif n>=3 and m>=7:
    print(m-2)
        