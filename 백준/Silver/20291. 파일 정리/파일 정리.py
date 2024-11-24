import sys
input = sys.stdin.readline

n = int(input())
files = {}

for _ in range(n):
  file = input().strip()
  l = file.split('.')
  if l[1] in files.keys():
    files[l[1]] += 1
  else:
    files[l[1]] = 1

result = dict(sorted(files.items()))

for key, value in result.items():
  print(key, value)