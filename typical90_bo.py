

N,K=map(int,input().split())

def anybase_to_decimal(x: int, k: int):
    '''
    x: n進数数字
    k: 変換元とする進数
    '''
    dec = 0
    for idx, ch in enumerate(reversed(str(x))):
        dec += int(ch) * (k**idx)
    return dec


def decimal_to_base(x: int, base: int) -> list:
    if x//base:
        return decimal_to_base(x//base, base) + [x%base]
    return [x%base]

n = N

for k in range(K):
    d = anybase_to_decimal(n, k=8)
    nine = decimal_to_base(d, base=9)
    chg = [5 if x == 8 else x for x in nine]
    chg = int("".join(map(str, chg)))
    n = chg

print(n)
