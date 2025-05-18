import math

def find_group(n):
  k = 1
  while (k * (k + 1)) // 2 < n:
      k += 1
  return k

t = int(input())

for i in range(t):
  n = int(input())
  group = find_group(math.ceil(n/26-1)+1) # 몫을 통해 그룹에 할당됨 (1->1, 3->2(반복 횟수))
  start = 13*((group-1)*group)  # 해당 그룹의 시작
  idx = n-start
  char = chr(math.ceil(idx/group)+64)
  print("Case #%d: %s" % (i+1, char))