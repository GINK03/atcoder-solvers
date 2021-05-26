import collections
org = list(input())

if len(set(org)) == 1:
    print(0)
    exit()


ans = float('inf')
for num in range(ord('a'), ord('z')+1):
    char = chr(num)
    cnt = 0
    s = org[:]
    while True:
        ns = []
        for i in range(len(s)-1):
            if s[i] == char or s[i+1] == char:
                ns.append(char)
            else:
                ns.append(s[i])
        cnt += 1
        s = ns
        if all([a==char for a in s]):
            break
    if s == []:
        continue
    #print(char, ns)
    ans = min(ans, cnt)
print(ans)



