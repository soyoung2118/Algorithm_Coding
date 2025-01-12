import sys

input = sys.stdin.readline
n = int(input())
tr = [list(map(int, input().split())) for _ in range(n)]

dp=[[0] * i for i in range(1, n+1)]
dp[0][0] = tr[0][0]

for i in range(1,n):
  for j in range(i+1):
    if j==0: 
      dp[i][j] = tr[i][j] + dp[i-1][0]
    elif j==i:
      dp[i][j] = tr[i][j] + dp[i-1][i-1]
    else:
      dp[i][j] = tr[i][j] + max(dp[i-1][j-1], dp[i-1][j])

result = max(dp[n-1])
print(result)