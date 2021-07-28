

S = input()

"""
 1. BCをDに変換する
 2. 余ったB,Cは転置数の末端になる
 3. 累積の転置数を数えれば良い
"""

S = S.replace("BC", "D")

ans = 0
d = 0
for i in range(len(S))[::-1]:
    if S[i] == 'A':
        ans += d
    elif S[i] == 'D':
        d += 1
    else:
        d = 0

print(ans)
