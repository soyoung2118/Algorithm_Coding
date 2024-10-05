n, m = map(int, input().split())

result = 1
div = 1

for i in range(m):
  result *= (n-i)
  div *= (i+1)

print(result//div)