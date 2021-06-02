
N=int(input())
*A,=map(lambda x:int(x)+1, input().split())

class BIT:
    def __init__(self, N):
        self.data = [0]*(N+1)
    def add(self, k, x):
        data = self.data
        while k <= N:
            data[k] += x
            k += k & -k
    def get(self, k):
        data = self.data
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s
b = BIT(N=N)

ans = 0
for i, a in enumerate(A):
    # 自分より小さい要素がいくつ存在するかを計算
    ans += (N-1-i) - b.get(a)
    b.add(a, 1)

for i in range(N):
    print(ans)
    # 先頭を取り除くことで省略できるコストA[i](左端からみたA[i]まで移動するコスト)
    # 末尾に追加するこてで追加されるコストN+1-A[i] (右端からみたA[i]まで移動するコスト)
    ans += N+1 - A[i]*2
