import sys
input = sys.stdin.readline

n = int(input())
placed = []
for i in range(n):
    q, m = map(int, input().split())
    placed.append((q, m))

placed_1 = sorted(placed, key=lambda x: (-x[0], x[1]))
placed_2 = sorted(placed, key=lambda x: (x[1], -x[0]))

for i in range(2): 
    for item in placed_1[i]:
        print(item, end=' ')
print() #줄바꿈

for j in range(2):  
    for item in placed_2[j]:
        print(item, end=' ')