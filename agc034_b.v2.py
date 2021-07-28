

S = input()

"""
 1. BCをDに変換する
 2. 余ったB,Cは転置数の末端になる
 3. 累積の転置数を数えれば良い
"""

S = S.replace("BC", "D")

class BIT:
    """
    入力されるリストの最小値は1以上である必要がある
    """
    def __init__(self, N):
        self.data = [0]*(N+1)
        self.N = N
    def add(self, k, x):
        data = self.data
        while k <= self.N:
            data[k] += x
            k += k & -k
    def get(self, k):
        data = self.data
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s
    def get_num(self, arr):
        num = 0
        for i, a in enumerate(arr):
            num += (self.N-1-i) - self.get(a)
            self.add(a, 1)
        return num

ans = 0
tmp = []
for i in range(len(S)):
    if S[i] in {"B", "C"}:
        try:
            b = BIT(len(tmp))
            ans += b.get_num(tmp)
        except:
            pass
        finally:
            tmp = []
    elif S[i] == "A":
        tmp.append(2)
    else:
        tmp.append(1)

try:
    b = BIT(len(tmp))
    ans += b.get_num(tmp)
except:
    pass
print(ans)
