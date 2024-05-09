import sys
input=sys.stdin.readline

n,k=map(int,input().split())

def function(n,k):
    up=1
    down=1
    result=0
    if k==0:
        result=1
        
    else:
        for i in range(n-k+1,n+1):
            up*=i
        for j in range(1,k+1):
            down*=j
        result=(up//down)%10007
    return result

print(function(n,k))