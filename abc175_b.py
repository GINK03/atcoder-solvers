import os

from itertools import combinations

n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for a, b, c in combinations(lst, 3):
    if a == b or b == c or c == a:
        continue
    if a + b > c and b + c > a and c + a > b:
        cnt += 1
print(cnt)
