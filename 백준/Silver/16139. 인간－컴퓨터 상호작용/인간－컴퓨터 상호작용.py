import sys
input = sys.stdin.readline

s = input()

arr = [[0]*len(s) for _  in range(26)]
for i in range(ord('a'),ord('z')+1):
  for j in range(len(s)):
    arr[i-97][j] = s.count(chr(i), 0, j)

q= int(input())

for _ in range(q):
  a, l, r = input().split()
  l, r = map(int, [l,r])
  cnt = arr[ord(a)-97][r+1] - arr[ord(a)-97][l] 
  print(cnt)