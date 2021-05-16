
X=int(input())
M=int(input())

D=max([int(a) for a in str(X)])

def anybase_to_decimal(x: int, k: int):
    '''
    x: n進数数字
    k: 変換元とする進数
    '''
    dec = 0
    for idx, ch in enumerate(reversed(str(x))):
        dec += int(ch) * (k**idx)
    return dec


def check(n):
    dec = anybase_to_decimal(x=X, k=n) 
    return dec <= M
 

if X < 10:
    print(int(D <= M))
    exit()

ok = D
ng = 10 ** 20
while(True):
  mid = (ok+ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid
  if ng - ok == 1:
    break
print(ok-D)
