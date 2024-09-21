n = int(input())  # 지방의 수
r = list(map(int, input().split()))  # 예산 요청 리스트
m = int(input())  # 총 예산

def assign(r, m):
    start, end = 0, max(r)  
    while start <= end:
        mid = (start + end) // 2  
        total = sum(min(req, mid) for req in r)  

        if total > m:  
            end = mid - 1
        else: 
            start = mid + 1
    return end 

print(assign(r, m))