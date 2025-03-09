import sys
input = sys.stdin.readline

n = int(input()) 
logs = {}  

for _ in range(n):
  name, record = input().split()
  if record == "enter":
    logs[name] = True
  elif record == "leave":
    if name in logs:
      del logs[name]  

remain = sorted(logs.keys(), reverse=True)

for name in remain:
    print(name)