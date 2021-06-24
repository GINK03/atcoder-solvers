N = int(input())
L = []
R = []
for _ in range(N):
    l, r = 0, 0
    s = input()
    for i in range(len(s)):
        if s[i] == "(":
            l += 1
        else:
            if l:
                l -= 1
            else:
                r += 1
    if l >= r:
        L.append([l, r])
    else:
        R.append([l, r])

L.sort(key=lambda x: x[1]) # Rが小さい順で並べる
R.sort(key=lambda x: -x[0]) # Lが大きい順で並び替える
arr = L + R
cnt = 0
for l, r in arr:
    if cnt < r:
        print("No")
        exit()
    cnt += l - r # 残りl数
if cnt == 0:
    print("Yes")
else:
    print("No")
