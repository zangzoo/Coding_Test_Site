x,y=map(int,input().split())
day=0
week=['SUN','MON','TUE','WED','THU','FRI','SAT']
mon=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(x-1):
    day+=mon[i]

day=(y+day)%7
print(week[day])
