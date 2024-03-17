import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

n_list.sort()

for num in m_list:
    exist=False
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if num==n_list[mid]:
            exist=True
            print(1)
            break
        elif num>n_list[mid]:
            start=mid+1
        else:
            end=mid-1
    if not exist:
        print(0)
