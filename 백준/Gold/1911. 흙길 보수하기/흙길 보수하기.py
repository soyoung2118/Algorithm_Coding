import sys
input = sys.stdin.readline

N, L = map(int, input().split())

puddles = []
for _ in range(N):
    puddles.append(list(map(int, input().split())))

puddles.sort()

endpoint=0
cnt = 0
for puddle in puddles:
  start = puddle[0]
  end = puddle[1]
  if start < endpoint:
    start = endpoint
  cnt += (end-start-1) // L + 1
  endpoint = start + L * ((end-start-1) // L + 1) 

print(cnt)