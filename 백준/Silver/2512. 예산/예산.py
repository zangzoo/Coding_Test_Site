import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input()) # 예산
start, end = 0, max(n_list) # 시작 점, 끝 점

# 이분 탐색
while start <= end:
    mid = (start+end) // 2
    total = 0 # 총 지출액
    for money in n_list:
        if money > mid: # 나라의 요청 예산이 현재의 상한액보다 크다면
            total += mid # 상한액 더해주기 => 상한액까지만 지출할 수 있으니까
        else: # 나라의 요청 예산이 현재의 상한액보다 작다면
            total += money # 나라의 요청예산 더해주기 => 상한액보다 작으니까 money지출가능
    if total <= m: # 총 지출액이 예산 보다 작으면
        start = mid + 1 
    else: # 총 지출액 예산 보다 크면
        end = mid - 1
print(end)