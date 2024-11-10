import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

k = int(input())
dp = [[0]*(m+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, m+1):
    dp[a][b] = dp[a][b-1] + dp[a-1][b] - dp[a-1][b-1] + lst[a-1][b-1]

for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])