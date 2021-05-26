S=input()

dp=[0]*(len(S)+2)

for i, s in enumerate(S,1):
    if s == '<':
        dp[i+1] = dp[i]+1

for i, s in reversed(list(enumerate(S,1))):
    if s == '>':
        #dp[i] = max(dp[i], dp[i+1]+1)
        dp[i] = max(dp[i], dp[i+1]+1)
#print(dp)

print(sum(dp))
    

