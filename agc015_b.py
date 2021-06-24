
S=input()
num = len(S)
 
ans = 0
for i in range(num):
    if S[i] == "U":
        ans += (num-i-1) + 2*i
    elif S[i] == "D":
        ans += 2*(num-i-1) + i
print(ans)
