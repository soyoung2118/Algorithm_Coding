t = int(input())

def find(x, parent):
  ps=[x]
  while parent[x]:
    ps.append(parent[x])
    x=parent[x]
  return ps

def common_anc(p1, p2):
  i=1
  if len(p1) > len(p2):
    p1=p1[len(p1)-len(p2):]
  elif len(p2) > len(p1):
    p2=p2[len(p2)-len(p1):]
  for a,b in zip(p1, p2):
    if a==b:
      return a

for _ in range(t):
  edge = {}
  n = int(input())
  parent = [0 for _ in range(n+1)]
  for _ in range(n-1):
    a, b = map(int, input().split())
    parent[b]=a
  n1, n2 = map(int, input().split())
  n1_ps = find(n1, parent)
  n2_ps = find(n2, parent)
  print(common_anc(n1_ps, n2_ps))
  