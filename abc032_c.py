N,K=map(int,input().split())

S=[]
for _ in range(N):
    S.append(int(input()))
if S.count(0) != 0:
    print(N)
    exit()

right = 0
calc = 1
ans = 0
for left in range(0,N):
    while right < N:
        if S[right]*calc <= K:
            calc *= S[right]
            ans = max(ans, right-left+1)
            #print(left, right, calc)
            right += 1
        else:
            break
    # leftがrightに追いついてしまったら
    # rightをインクリメントする
    # (これを入れ忘れると間違う)
    if left == right:
        right += 1
    else:
        # インクリメント時に前の情報を消す
        calc /= S[left]

print(ans)

