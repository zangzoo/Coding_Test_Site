import sys
input=sys.stdin.readline().rstrip

n=input()
n_i=[]
exist_0=False
for i in n:
    n_i.append(int(i))
    if i=='0':
        exist_0=True

if exist_0==True and sum(n_i)%3==0:
    n_i.sort(reverse=True)
    for i in n_i:
        print(i,end='')
else:
    print(-1)