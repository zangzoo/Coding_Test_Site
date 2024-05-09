import sys
input=sys.stdin.readline

n,m=map(int,input().split())
d=int(input())
arr=[[0 for _ in range(m+1)] for _ in range(n+1)]
result=0

# 효석이가 왼쪽 위 모서리일때, 왼쪽 위 모서리에서 택시 거리 D 미만인 칸들 1로 설정
for i in range(1,n+1):
    for j in range(1,m+1):
        if abs(1-i)+abs(1-j)<d:
            arr[i][j]=1
            
# 효석이가 오른쪽 위 모서리일때, 오른쪽 위 모서리에서 택시 거리 D 미만이고 1로 설정된 칸들 2로 설정
for i in range(1,n+1):
    for j in range(1,m+1):
        if abs(1-i)+abs(m-j)<d and arr[i][j]==1:
            arr[i][j]=2
           
# 효석이가 왼쪽 아래 모서리일때, 왼쪽 아래 모서리에서 d미만이고, 2로 설정된 칸들 3으로 설정
for i in range(1,n+1):
    for j in range(1,m+1):
        if abs(n-i)+abs(1-j)<d and arr[i][j]==2:
            arr[i][j]=3
    
# 효석이가 오른쪽 아래 모서리일때, 오른쪽 아래 모서리에서 d미만이고, 3으로 설정된 칸들 4로 설정
for i in range(1,n+1):
    for j in range(1,m+1):
        if abs(n-i)+(m-j)<d and arr[i][j]==3:
            result+=1
            
print(result)            