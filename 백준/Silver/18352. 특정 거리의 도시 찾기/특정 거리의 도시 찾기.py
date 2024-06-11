from collections import deque
import sys
input=sys.stdin.readline

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    
distance=[-1]*(n+1)
distance[x]=0 # 출발 도시까지의 거리는 0으로 설정

#bfs 수행
q=deque([x])
while q:
    now=q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next in graph[now]:
        # 아직 방문안한 도시면
        if distance[next]==-1:
            # 최단 거리 갱신
            distance[next]=distance[now]+1
            q.append(next)
            
# 최단 거리가 k인 모든 도시의 번호 오름차순 출력
check = False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
        
# k인 도시 없으면 -1 출력
if check==False:
    print(-1)