# 2021/05/23
# かなり難しい気がする

import math
 
a, b, k = map(int, input().split())
ans = ""
 
for i in range(a + b):
    ref = math.comb(a + b - 1, b)
    if k <= ref:
        ans = ans + "a"
        a -= 1
    else:
        k -= ref
        ans = ans + "b"
        b -= 1
 
print(ans)
