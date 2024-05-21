import sys
import math
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))

up = a.pop(-1)
down = up * a.pop(-1)+1

while len(a)>0:
    up=a.pop(-1)*down + up
    up,down=down,up

up= down-up

if math.gcd(up,down)!=1:
    down,up=down//math.gcd(down,up), up//math.gcd(down,up)
    
print(up,down)