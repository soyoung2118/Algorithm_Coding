for _ in range(int(input())):
  cnt = 0
  idx = 0

  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  a.sort()
  b = list(map(int, input().split()))
  b.sort() 

  for i in a:
    while idx < m:
      if i > b[idx]:
        idx += 1
      else:
        break
    cnt += idx
  print(cnt)
