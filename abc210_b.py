
import collections
N = int(input())
S = list(map(int,input()))
S = collections.deque(S)

cnt = 0
while S:
    f = S.popleft()
    if cnt%2 == 0 and f == 1:
        print("Takahashi")
        break
    elif f == 1:
        print("Aoki")
        break
    cnt +=1
