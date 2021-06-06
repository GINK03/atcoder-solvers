
N=int(input())
*A,=map(int,input().split())


tmp = set([A[0]]) # index 0が初期値になる
ans = len(tmp)

left, right = 0,0 # 動かす変数
while right+1 <= N-1: # 右がはみ出たら終了
    if A[right+1] not in tmp: # right+1を伸ばせるところまで伸ばす
        tmp.add(A[right+1])
        right += 1
    else: # rightが無理だったらleftを掃除してleft+1へインクリメント
        tmp.remove(A[left])
        left += 1
    ans = max(ans, len(tmp))
print(ans)
