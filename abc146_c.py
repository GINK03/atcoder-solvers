
A,B,X=map(int,input().split())

def check(n):
    return A*n + B*len(str(n)) <= X and n <= 10**9
 
ok = 0
ng = 10 ** 20
while(True):
  mid = (ok+ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid
  if ng - ok == 1:
    break
print(ok)
