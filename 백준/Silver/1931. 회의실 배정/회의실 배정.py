import sys
input=sys.stdin.readline

t=[]
n=int(input())
for i in range(n):
    start,end=map(int,input().split())
    t.append((start,end))

# 회의 시간을 종료 시간 기준 및 시작 시간 기준으로 정렬
t.sort(key=lambda x: (x[1],x[0]))
cnt=1
end=t[0][1]

for i in range(1,n):
    # 다음 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같다면
    if t[i][0]>=end:
        # 이전 회의 종료 시간 업데이트
        end=t[i][1]
        cnt+=1

print(cnt)