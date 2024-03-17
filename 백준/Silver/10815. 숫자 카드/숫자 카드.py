import sys
input=sys.stdin.readline

n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

dic={}

for i in n_list:
    dic[i]=0
for j in m_list:
    if j not in dic:
        print(0, end=' ')
    else:
        print(1, end=' ')