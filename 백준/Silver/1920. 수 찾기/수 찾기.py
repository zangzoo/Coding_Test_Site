import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

n_list_2=sorted(n_list)

for i in m_list:
    start=0
    end=n-1
    exist=False

    while start<=end:
        mid=(start+end)//2
        if i == n_list_2[mid]:
            exist=True
            print(1)
            break
        elif i>n_list_2[mid]: #찾고자 하는 m이 더 크면
            start=mid+1
        else:
            end=mid-1
    if not exist:
        print(0)