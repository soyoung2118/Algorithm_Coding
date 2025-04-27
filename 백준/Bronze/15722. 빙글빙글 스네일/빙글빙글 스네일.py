n = int(input())
x = 0
y = 0
step = 1    
time = 0    
dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while time < n:
    for _ in range(step):
        if time == n:
            break
        x += dx[dir]
        y += dy[dir]
        time += 1

    dir = (dir + 1) % 4  

    if dir % 2 == 0:
        step += 1

print(x, y)