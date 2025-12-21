left = ['q','w','e','r','t','g','a','s','d','f','z','x','c','v']
keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]


def find(x):
  for i, row in enumerate(keyboard):
    for j, value in enumerate(row):
      if value==x:
        return (i,j)

sl,sr = input().split()
string = input()
sl=find(sl)
sr=find(sr)

total=0

for a in string:
  pos = find(a)
  if a in left:
    total+=abs(sl[0] - pos[0]) + abs(sl[1] - pos[1]) + 1
    sl=pos
  else:
    total+=abs(sr[0] - pos[0]) + abs(sr[1] - pos[1]) + 1
    sr=pos

print(total)
