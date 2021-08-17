
from collections import Counter
H, W = map(int, input().split())
 
S = Counter()
for h in range(H):
    row = input()
    S += Counter(row)
 
def main(S, H, W):
    mult4 = 0
    odds = 0
    for s, count in S.items():
        q, r = divmod(count, 4)
        mult4 += q
        if count % 2 == 1:
            odds += 1
 
    if mult4 < (H//2) * (W//2):
        return "No"
    elif odds > 1:
        return "No"
    elif odds == 1 and H%2 == 0 and W%2 == 0:
        return "No"
    else:
        return "Yes"
 
 
print(main(S, H, W))
