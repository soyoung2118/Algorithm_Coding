t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  if n>m: 
    print("No")
  else:
    print("Yes")