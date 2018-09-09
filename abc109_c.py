from functools import reduce

def gcd(*numbers):
    from math import gcd
    return reduce(gcd, numbers)

def lcm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

N, X = map(int, input().split() )

xs = [ int(x) for x in input().split() ] 

left =  list(reversed([abs(x-X) for x in list(filter(lambda x:x <= X, xs))] + [0] ))
right = [x-X for x in ([X] + [x for x in list(filter(lambda x:x >= X, xs))]) ]
#print(left)
#print(right)

stocks = set()
for d in range(1,len(right)):
  stocks.add( right[d] - right[d-1] )
for d in range(1,len(left)):
  stocks.add( left[d] - left[d-1] )
print(stocks)
print(lcm(*list(stocks)))
