from collections import deque

n,k=map(int,input().split())

graph=[] #전체 보드 정보
data=[] #바이러스 정보

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        # 해당 위치에 바이러스 있으면
        if graph[i][j]!=0:
            # (바이러스 종류, 시간, x,y) 삽입
            data.append((graph[i][j],0,i,j))

#정렬 => 낮은 번호 바이러스 먼저 증식하도록
data.sort()
q=deque(data)

target_s,target_x,target_y=map(int,input().split())

#상하좌우 이동 방향 설정
dx=[0,0,-1,1]
dy=[1,-1,0,0]

#bfs 진행
while q:
    virus,s,x,y=q.popleft()
    # s초 됐거나, 큐가 빌때까지 반복
    if s==target_s:
        break
    # 현재 노드에서 상하좌우 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #해당 위치로 이동할 수 있으면
        if 0<=nx and nx<n and 0<=ny and ny<n:
            #아직 방문하지 않은거면 바이러스 넣기
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))
                
print(graph[target_x-1][target_y-1])