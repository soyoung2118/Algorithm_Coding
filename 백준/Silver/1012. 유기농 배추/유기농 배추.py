import sys
sys.setrecursionlimit(10000)

t = int(input())

def dfs(x, y):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<m and 0<=ny<n and g[ny][nx] == 1:
      g[ny][nx] = 0
      dfs(nx,ny)

for _ in range(t):
  m, n, k  = map(int, input().split())
  g = [[0]*m for _ in range(n)]
  cnt = 0

  for _ in range(k):
    x, y = map(int, input().split())
    g[y][x] = 1

  for i in range(m):
    for j in range(n):
      if g[j][i] == 1:
        dfs(i, j)
        cnt += 1

  print(cnt)