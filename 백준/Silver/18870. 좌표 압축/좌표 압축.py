import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
sort_lst = sorted(list(set(lst)))

index_map = {value: idx for idx, value in enumerate(sort_lst)}

for i in range(N):
  print(index_map[lst[i]])