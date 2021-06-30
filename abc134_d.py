
N = int(input())
A = list(map(int, input().split()))
 
balls = [-1]*N
 
for i in range(N, 0, -1):
    # iの倍数の箱についてパリティがA[i]と一致するようにballsを設定
    cnt = 0
    for j in range((N//i)*i, 0, -i):
        if balls[j-1] != -1:
            cnt += balls[j-1]
        else:
            balls[j-1] = (cnt + A[i-1]) % 2
            break
 
m = sum(balls)
print(m)
if m > 0:
    for i in range(1,N+1):
        if balls[i-1] == 1:
            print(i, '', end='')
    print('')



