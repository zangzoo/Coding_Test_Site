import sys
input=sys.stdin.readline

k,n=map(int,input().split())
k_cm=[] 

for _ in range(k):
    k_cm.append(int(input()))

start = 1
end = max(k_cm)

while start<=end:
    k_count = 0
    mid = (start+end)//2
    for cm in k_cm:
        k_count += cm//mid
    if k_count >= n:
        start = mid +1
    else:
        end = mid-1
print(end)