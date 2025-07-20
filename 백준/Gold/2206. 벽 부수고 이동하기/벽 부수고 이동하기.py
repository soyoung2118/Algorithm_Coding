import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0,0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,z):
  queue = deque()
  queue.append((x,y,z))

  while queue:
    a, b, c = queue.popleft()
    if a == n-1 and b == m-1: 
      return visited[a][b][c]

    for i in range(4):
      nx = a+dx[i]
      ny = b+dy[i]

      if 0<=nx<n and 0<=ny<m:  # 유효한 위치 

        if graph[nx][ny]==1 and c==0:  # 벽o & 벽파괴x
          visited[nx][ny][1] = visited[a][b][0] + 1
          queue.append((nx, ny, 1))
        elif graph[nx][ny]==0 and visited[nx][ny][c]==0:  # 방문x & 벽x
          visited[nx][ny][c] = visited[a][b][c] + 1
          queue.append((nx, ny, c))
    
  return -1

print(bfs(0, 0, 0))