from string import ascii_lowercase

S = input()
K = int(input())

ans=[]
for c in S:
    if c == 'a':
        ans.append('a')
        continue
    if ord('z') +1 - ord(c) > K:
        ans.append(c)
    else:
        ans.append('a')
        K -= ord('z') + 1 - ord(c)
if K > 0:
    K = K % 26
    ans[-1] = chr(ord(ans[-1])+K)

print(*ans, sep="")
