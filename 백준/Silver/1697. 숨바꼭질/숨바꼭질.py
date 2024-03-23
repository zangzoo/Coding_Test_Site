import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
visited=[0 for _ in range(100001)]

def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft()
        if v==k: #만약 동생을 찾았다면
            return visited[v] #방문리스트의 v 인덱스= 움직인 시간 출력
        for i in (v-1,v+1,2*v):
            if 0<=i<=100000 and not visited[i]:
                visited[i]=visited[v]+1 
                q.append(i)

print(bfs(n))