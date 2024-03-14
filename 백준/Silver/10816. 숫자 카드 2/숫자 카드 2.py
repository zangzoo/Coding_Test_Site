import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_counter = Counter(n_list)  # n_list의 각 숫자의 개수를 세는 Counter 객체 생성

result = []
for num in m_list:
    result.append(n_counter[num])  # m_list에 있는 각 숫자의 개수를 n_list에서 찾아서 저장

print(' '.join(str(count) for count in result))
