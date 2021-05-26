import math
import itertools
X=int(input())

if X==1:
    print(1)
    exit()

ans = 0 
for x in reversed(range(2,X)):
    for p in itertools.count(2):
        if pow(x,p) <= X:
            ans = max(ans, pow(x,p))
        else:
            break
print(ans)
