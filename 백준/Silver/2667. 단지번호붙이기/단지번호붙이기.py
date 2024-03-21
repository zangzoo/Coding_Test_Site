n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
count = 0
all_counts = []

def dfs(x, y):
    global count #count 전역변수로 설정해야함!!!!
    if x == -1 or y == -1 or x == n or y == n:
        return False # 맵 벗어나면 종료시키기
    elif graph[x][y] == 1: # 만약 노드가 1이라면
        graph[x][y] = 0 # 0으로 바꿔주기 => 방문처리
        count += 1 # 단지별 집의 수 count
        dfs(x + 1, y) #상하좌우 재귀함수
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        return True
    return False #만약 노드가 0이라면 => 종료시킴

for i in range(n): 
    for j in range(n):
        if dfs(i, j): # n*n맵 돌아다니며 dfs수행 
            all_counts.append(count) # all_count리스트에 count값 추가
            count = 0

all_counts.sort() #리스트 정렬 => 오름차순
print(len(all_counts)) #단지수 출력
for c in all_counts:
    print(c) #각 단지별 집 수 출력
