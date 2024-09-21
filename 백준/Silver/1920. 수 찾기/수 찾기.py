n = int(input())
l1 = list(map(int, input().split()))
l1.sort()
m = int(input())
l2 = list(map(int, input().split()))
y=[]

def bs(x):
  start = 0
  end = n-1

  while start <= end:
    mid = (start+end)//2
    if(x==l1[mid]):
      return 1
    elif(x < l1[mid]):
      end = mid-1
    elif(x > l1[mid]):
      start = mid+1

  return 0

for i in range(m):
  print(bs(l2[i]))