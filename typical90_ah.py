import collections
N,K=map(int,input().split())
*A,=map(int,input().split())

left, right = 0, 0
Map = collections.defaultdict(int)
shurui, ans = 0, = 0

while left < N:
    while right < N:
        if Map[A[right]] == 0 and shurui == K: # break条件を最初に
            break
        if Map[A[right]] == 0:
            shurui += 1
        Map[A[right]] += 1
        right += 1 # インクリメントは最後　
    ans = max(ans, right - left)
    if Map[A[left]] == 1:
        shurui -= 1
    Map[A[left]] -= 1
    left += 1 # インクリメントは最後

print(ans) 


