import sys
input=sys.stdin.readline

crane_num=int(input())
crane_weight=list(map(int,input().split()))
box_num=int(input())
box_weight=list(map(int,input().split()))

crane_weight.sort(reverse=True)
box_weight.sort(reverse=True)

cnt=0

if box_weight[0]>crane_weight[0]:
    cnt = -1
else:
    while len(box_weight)>0:
        for crane in crane_weight:
            if box_weight and crane < box_weight[-1]:
                continue
            for box in box_weight:
                if crane >= box:
                    box_weight.remove(box)
                    break
        cnt+=1
        
print(cnt)