n=int(input())

start=n//5
  
for i in range(start,-1,-1):
    rest=n-(5*i)
    if rest==0:
        print(int(i))
        break
    else:
        if rest%3==0:
            print(int(i+(rest/3)))
            break
else:
    print(-1)