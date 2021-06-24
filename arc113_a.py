
K = int(input())

"""
a*b*c = K
a*b = K/c
K >= c >=1 -> a*b <= K
 -> a <= K / b ; aの上界
"""


acc = 0
for b in range(1, K+1):
    for a in range(1, (K//b) + 1):
        c_num = K // (a*b)
        acc += c_num
print(acc)
