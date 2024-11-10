import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())
arr = []
dp = [[0]*(c+1) for _ in range(r+1)]

for _ in range(r):
  l = list(map(int, input().split()))
  arr.append(l)

for i in range(1,r+1):
  for j in range(1,c+1):
    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(q):
  r_1, c_1, r_2, c_2 = map(int, input().split())
  result = dp[r_2][c_2] - dp[r_2][c_1-1] - dp[r_1-1][c_2] + dp[r_1-1][c_1-1]
  print(result//((r_2-r_1+1)*(c_2-c_1+1)))