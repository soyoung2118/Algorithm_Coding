import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
region = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
  for m in range(4):
    nx = x + dx[m]
    ny = y + dy[m]
    if (0 <= nx < n) and (0 <= ny < n) and region[nx][ny] > h and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx, ny, h)


result = 1
for k in range(max(map(max, region))):   
    visited = [[False]*n for _ in range(n)]  
    count = 0
    for i in range(n):
        for j in range(n):
            if region[i][j] > k and not visited[i][j]: 
                count += 1
                visited[i][j] = True
                dfs(i, j, k)
    result = max(result, count)

print(result)