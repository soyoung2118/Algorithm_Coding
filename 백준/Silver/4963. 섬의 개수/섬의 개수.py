import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [-1, 0, 1, -1, 1, -1, 0, 1]
  dy = [-1, -1, -1, 0, 0, 1, 1, 1]

  for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<w and 0<=ny<h and square[ny][nx] == 1:
      square[ny][nx] = 0
      dfs(nx,ny)

while True:
  w, h = map(int, input().split())
  if w==0 and h==0:
    break

  square = []
  cnt = 0
  for _ in range(h):
    square.append(list(map(int, input().split())))
  for i in range(w):
    for j in range(h):
      if square[j][i] == 1:
        dfs(i, j)
        cnt += 1
  print(cnt)