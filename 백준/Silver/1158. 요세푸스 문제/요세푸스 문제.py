from collections import deque
n,k=map(int,input().split())
q=deque()
answer=[]

for i in range(1,n+1):
    q.append(i)

while q:
    for i in range(1,k):
        del_q=q.popleft()
        q.append(del_q)
    answer.append(q.popleft())

print('<',end='')
for i in range(0,len(answer)-1):
    print(answer[i],end=', ')
print(str(answer[-1])+'>')

#    <3, 6, 2, 7, 5, 1, 4>