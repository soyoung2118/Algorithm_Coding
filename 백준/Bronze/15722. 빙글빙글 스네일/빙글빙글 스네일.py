n = int(input())

x = 0
y = 0
step = 1     # 현재 이동 거리
moved = 0    # 현재까지 이동한 횟수
dir = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while moved < n:
    for _ in range(step):
        if moved == n:
            break
        x += dx[dir]
        y += dy[dir]
        moved += 1

    dir = (dir + 1) % 4  # 시계 방향 전환

    # 방향 2번마다 step 증가
    if dir % 2 == 0:
        step += 1

print(x, y)
