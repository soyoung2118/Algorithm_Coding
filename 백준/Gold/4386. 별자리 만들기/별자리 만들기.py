import math 

n = int(input())
stars = []
for _ in range(n):
  x, y = map(float, input().split())
  stars.append([x,y])

def dist(a,b):
  x1, y1 = stars[a]
  x2, y2 = stars[b]
  dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  return dist

visited = [False] * n
min_edge = [float('inf')] * n
min_edge[0] = 0.0

total = 0.0
for _ in range(n):
  u = -1
  best = float('inf')
  for i in range(n):
    if not visited[i] and min_edge[i] < best:
      best = min_edge[i]
      u = i

  visited[u] = True
  total += best

  for j in range(n):
    if not visited[j]:
      w = dist(u, j)
      if w < min_edge[j]:
        min_edge[j] = w

print(f"{total:.2f}")
 
