s=input()

size=len(s)

ans = float('inf')
for i in range(size-2):
    ans = min(ans,abs(753-int(s[i:i+3])))
print(ans)
