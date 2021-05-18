
def sieve(arr):
    max_ = max(arr)
    is_baisu = [0 for _ in range(max_+1)]

    for a in arr:
        is_baisu[a] += 1
        for b in range(a*2, max_+1, a):
            is_baisu[b] += 1
    cnt = 0
    for a in arr:
        # is_baisu[a] == 1であることは、一度しかその変数で作られておらず、他の数の倍数で表現できないということ
        if is_baisu[a] == 1:
            cnt += 1
    print(cnt)

N=input()
A=list(map(int,input().split()))
sieve(A)
