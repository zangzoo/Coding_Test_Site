from collections import deque
n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) #무방향 그래프

visited=[False]*(n+1)

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    q= deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        graph[v].sort
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

dfs(graph,v,visited)
print()  # 줄 바꿈

# BFS 실행을 위해 방문 여부 초기화
visited = [False] * (n + 1)

bfs(graph,v,visited)