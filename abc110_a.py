
xs = sorted(list(map(int, input().split())))

xs = list(reversed(xs))
#print(xs)
head = int( ''.join([str(x) for x in xs[0:2]]) )
tail = xs[-1]

print(head + tail)
