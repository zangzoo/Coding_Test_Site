import sys
input=sys.stdin.readline

n,m=map(int,input().split())
tree_h = list(map(int,input().split()))
start=0
end=max(tree_h)

while start<=end:
    mid=(start+end)//2
    tree_cut=0
    
    for i in tree_h:
        if i>mid:
            tree_cut+=i-mid
    if tree_cut < m:
        end=mid-1
    else:
        start=mid+1

print(end)

