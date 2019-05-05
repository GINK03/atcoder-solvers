n = int(input())
ws = [int(w) for w in input().split()]

mined = float('inf')
for i in range(1, len(ws)):
    h,t = ws[0:i], ws[i:]
    mined = min(mined, abs(sum(h) - sum(t)))
print(mined)
