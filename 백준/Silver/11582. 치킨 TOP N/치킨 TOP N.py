import math

n = int(input()) 
lst = list(map(int, input().split())) 
k = int(input())  

group_size = n // k

for i in range(0, n, group_size):
    lst[i:i + group_size] = sorted(lst[i:i + group_size])

print(*lst)