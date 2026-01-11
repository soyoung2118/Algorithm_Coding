def dist(x1, y1, x2, y2):
  return (x1-x2)**2 + (y1-y2)**2

t = int(input())

for _ in range(t):
  x_lst = []
  y_lst = []
  for _ in range(4):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
  d = []
  for i in range(4):
      for j in range(i + 1, 4):
          d.append(dist(x_lst[i], y_lst[i], x_lst[j], y_lst[j]))

  d.sort()

  if d[0] == d[1] == d[2] == d[3] and d[4] == d[5] == 2 * d[0]:
      print(1)
  else:
      print(0)