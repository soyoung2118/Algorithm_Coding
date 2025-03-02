import sys

N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

sort_lst = sorted(set(lst))  
index_map = {value: idx for idx, value in enumerate(sort_lst)} 

print(' '.join(map(str, (index_map[x] for x in lst)))) 