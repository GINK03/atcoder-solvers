

N = int(input())
*A,=map(int,input().split())

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

b = BIT(N=N)
print(b.get_num(A))
