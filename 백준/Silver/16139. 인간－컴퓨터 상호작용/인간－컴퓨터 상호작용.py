import sys
input = sys.stdin.readline

s = input()
q= int(input())

for _ in range(q):
  a, l, r = input().split()
  l, r = map(int, [l,r])
  cnt = s.count(a, l, r+1)
  print(cnt)