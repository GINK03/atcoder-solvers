
a = int(input())

b = ['Christmas']
c = ['Eve'] * (25 - a)
b.extend(c)
print(' '.join(b))
