a, b = map(int, input().split())
c, d = map(int, input().split())

# 전체 구간에서 소수를 직접 판별하여 구하기
x = min(a, c)
y = max(b, d)

all_prime = []
for i in range(x, y + 1):
    if i < 2:
        continue
    if i == 2:  # 2는 소수
        all_prime.append(i)
        continue
    if i % 2 == 0:  # 짝수는 소수가 아님
        continue
    is_prime = True
    for j in range(3, int(i ** 0.5) + 1, 2):  # 홀수로만 나눔
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        all_prime.append(i)

# 구간 별 소수 개수
yt = [k for k in all_prime if a <= k <= b]
yj = [k for k in all_prime if c <= k <= d]
cmn = [k for k in yt if k in yj]

yt_cnt = len(yt) - len(cmn)
yj_cnt = len(yj) - len(cmn)
cmn_cnt = len(cmn)

# 승패 판별
if cmn_cnt % 2 == 1:
    if yt_cnt >= yj_cnt:
        print("yt")
    else:
        print("yj")
else:
    if yt_cnt > yj_cnt:
        print("yt")
    else:
        print("yj")