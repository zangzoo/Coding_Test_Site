import sys
input=sys.stdin.readline

n=int(input())
l=list(map(int,input().split()))
gold=0
l.sort(reverse=True)

for i in range(1,len(l)):
    gold+=l[0]+l[i]
    
print(gold)