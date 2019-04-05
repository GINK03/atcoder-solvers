
N = int(input())
Hs = [int(x) for x in input().split()]

now_max_height = 0
viewable = 0
for i in range(N):
    if Hs[i] >= now_max_height:
        viewable += 1   
        now_max_height = Hs[i]


print(viewable)
