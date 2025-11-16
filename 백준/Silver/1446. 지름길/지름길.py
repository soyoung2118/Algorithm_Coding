N, D = map(int, input().split())

shortcuts = [[] for _ in range(D + 1)] 
for _ in range(N):
    s, e, w = map(int, input().split())
    if e > D:
      continue 
    shortcuts[s].append((e, w))

INF = 10**9
dist = [INF]*(D + 1)
dist[0] = 0  

for x in range(D):
    # 일반 도로 
    dist[x + 1] = min(dist[x + 1], dist[x] + 1)

    # x에서 시작하는 지름길
    for end, w in shortcuts[x]:
        dist[end] = min(dist[end], dist[x] + w)

print(dist[D])
