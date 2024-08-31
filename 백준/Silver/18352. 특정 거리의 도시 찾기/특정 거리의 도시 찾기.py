import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph=[[] for _ in range(N + 1)]
y = []  # 정답 리스트
d = [-1]*(N+1)  # 노드 간 거리 초기화
d[X]=0  # 시작 노드의 거리 0으로 설정

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([X]) 

while q:
    v = q.popleft()
    for i in graph[v]:
        if d[i]==-1:
            d[i] = d[v]+1
            q.append(i)
            if d[i]==K:
                y.append(i)

if len(y)==0:
    print(-1)
else:
    y.sort()
    for j in range(len(y)):
        print(y[j])