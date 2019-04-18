
N, Q = map(int, input().split())
S = input()
'''
この発送がなかなか出ない
'''
t = [0] * (N + 1)

for i in range(N):
    t[i + 1] = t[i] + (1 if S[i : i + 2] == 'AC' else 0)
'''
こうすると計算オーダーが落ちる
'''
for i in range(Q):
    l, r = map(int, input().split())
    print(t[r-1] - t[l-1])
