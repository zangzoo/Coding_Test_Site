import sys
sys.setrecursionlimit(10000)

t=int(input())

def dfs(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False
    elif graph[r][c] == 1:
        graph[r][c] = 0
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        return True
    return False

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
  
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                cnt += 1

    print(cnt)