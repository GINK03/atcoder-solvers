import itertools
H=int(input())
'''
cnt = 0
def check(h):
    global cnt
    cnt += 1
    if h == 1:
        return "end"
    if h > 1:
        check(h//2)
        check(h//2)

check(H)
print(cnt)
'''

h = H
for cnt in itertools.count(1):
    if h//2 > 0:
        h//=2
    else:
        # print(cnt)
        print(2**cnt-1)
        break
