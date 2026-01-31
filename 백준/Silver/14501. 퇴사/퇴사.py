n = int(input())

T = []
P = []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# DP 배열 생성
d = [0]*(n+1)

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사일을 넘기는 경우
    if i + T[i] > n:
        d[i] = d[i+1]
    else:
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것을 선택
        d[i] = max(d[i+1], P[i] + d[i + T[i]])

print(d[0])
