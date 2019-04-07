
anths = []
for i in range(5):
    anths.append(int(input()))
k = int(input())
from itertools import combinations

for a, b in combinations(anths, 2):
    if abs(a-b) > k:
        print(":(")
        exit()

print('Yay!')
