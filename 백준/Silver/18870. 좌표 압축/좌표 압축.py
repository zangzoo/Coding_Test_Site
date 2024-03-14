import sys
input=sys.stdin.readline

n=int(input())
x=list(map(int,input().split()))
x_sorted= sorted(list(set(x)))

dic={x_sorted[i] : i for i in range(len(x_sorted))}
for j in x:
    print(dic[j],end=' ')
