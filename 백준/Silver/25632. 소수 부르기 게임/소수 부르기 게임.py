a, b = map(int, input().split())
c, d = map(int, input().split())

# 전체 구간의 소수 개수 구하기
x = min(a, c)
y = max(b, d)
is_prime = [True] * (y + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(y ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, y + 1, i):
            is_prime[j] = False

# 소수 리스트 생성
all_prime = [i for i in range(x, y + 1) if is_prime[i]]

# 구간 별 소수 개수
yt = [k for k in all_prime if a<=k<=b]
yj = [k for k in all_prime if c<=k<=d]
cmn = [k for k in yt if k in yj]

yt_cnt = len(yt) - len(cmn)
yj_cnt = len(yj) - len(cmn)
cmn_cnt = len(cmn)

# 승패
if cmn_cnt % 2 ==1:
  if yt_cnt >= yj_cnt:
    print("yt")
  else:
    print("yj")
else:
  if yt_cnt > yj_cnt:
    print("yt")
  else:
    print("yj")