board = [list(map(int, input().split())) for _ in range(5)]
r, c= map(int, input().split())

def check(x, y, move, apple):
  if move > 3: 
    return 0
  if apple >= 2:  
    return 1

  temp = board[x][y]
  board[x][y] = -1

  lst = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
  result = 0
  for i, j in lst:
    if 0 <= i < 5 and 0 <= j < 5 and board[i][j] != -1:
      if board[i][j] ==1:
        z = 1
      else:
        z = 0
      result = check(i, j, move+1, apple+z)
      if result == 1:
        break
  
  board[x][y] = temp
  return result

if check(r, c, 0, 0) == 1:
  print("1")
else:
  print("0")