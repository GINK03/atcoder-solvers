
x = input()

base = int(x)

xs = [x for x in [int(c*3) for c in set('123456789') ] if x >= base ]
print(sorted(xs).pop(0))


