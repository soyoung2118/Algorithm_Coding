from collections import deque

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

def bfs(start):
  visited = [False] * (n + 1)
  dist = [0] * (n + 1)
  queue = deque([start])
  visited[start] = True

  while queue:
    x = queue.popleft()
    for friend in friends[x]:
      if not visited[friend]:
        visited[friend] = True
        dist[friend] = dist[x] + 1
        queue.append(friend)

  return sum(dist)

result = []
for i in range(1, n + 1):
  total = bfs(i)
  result.append(total)

print(result.index(min(result)) + 1)