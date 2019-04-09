
N = int(input())
min_ = min([int(input()) for i in range(5)])

suf = 1 if N%min_ != 0 else 0
print(N//min_+4+suf)
