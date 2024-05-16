n=int(input())
placed=[]
for i in range(n):
    q,m=map(int,input().split())
    placed.append((q,m))

placed_1=sorted(placed, key=lambda x:(-x[0],x[1]))
placed_2=sorted(placed, key=lambda x:(x[1],-x[0]))
result_1=[]
result_2=[]
for i in placed_1[0]:
    result_1.append(i)
for i in placed_1[1]:
    result_1.append(i)
for i in placed_2[0]:
    result_2.append(i)
for i in placed_2[1]:
    result_2.append(i)
    
for i in result_1:
    print(i,end=' ')
for i in result_2:
    print(i,end=' ')
    