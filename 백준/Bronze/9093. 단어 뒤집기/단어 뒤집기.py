t = int(input())
 
for _ in range(t):
    words = input().split()
 
    for word in words:
        print(word[::-1], end=' ')
print()