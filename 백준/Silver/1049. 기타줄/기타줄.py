n, m = map(int, input().split())

min_pkg = 1000
min_item = 1000

for _ in range(m):
  pkg, item =  map(int, input().split())
  min_pkg = min(min_pkg , pkg)
  min_item = min(min_item, item)

price = min(min_pkg*(n//6)+min_item*(n%6), min_pkg*(n//6+1), min_item*n)
print(price)