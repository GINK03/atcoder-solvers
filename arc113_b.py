
import collections

A, B, C = map(int, input().split())

def exponent(n,k):
    if k == 1: return n % 4
    if k % 2 == 1: return (exponent(n,k//2) * exponent(n,k//2+1))%4
    return (exponent(n,k//2) ** 2) % 4
BC = exponent(B,C) + 4

    
# p = pow(A,BC, 10)
print(p)
