import sys
input=sys.stdin.readline().rstrip

n=input()

if '0' not in n:
    print(-1)
else:
    n_sum=0
    for i in range(len(n)):
        n_sum+=int(n[i])
    if n_sum%3 !=0:
        print(-1)
    else:
        sorted_n=sorted(n,reverse=True)
        answer=''.join(sorted_n)
        print(answer)
       