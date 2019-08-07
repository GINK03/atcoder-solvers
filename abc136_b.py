x = int(input())
import math
c = 0
for i in range(1, x+1):
    if int(math.log10(i))%2 == 0:
        c+=1
print(c)
