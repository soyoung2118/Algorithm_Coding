n = int(input())
temp = []

def valid(temp,i):
  j = len(temp)
  for r in range(j): 
    if temp[r]==i or abs(temp[r]-i)==abs(r-j):  # 같은 열이거나 대각선에 있을 경우, False 반환 
      return False
  return True

def backtrack():
  ans=0
  if len(temp)==n:
    return 1
  for i in range(n):
    if valid(temp, i):
      temp.append(i)
      ans += backtrack()
      temp.pop()
  return ans

ans = backtrack()
print(ans)