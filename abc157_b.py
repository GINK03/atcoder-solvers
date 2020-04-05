
xs = []
for i in range(3):
    x = list(map(int,input().split()))
    xs.append(x)

n = int(input())
bs = {int(input()) for i in range(n)}

for i in range(3):
    xs[i] = [x in bs for x in xs[i] ]


flags = []
for i in range(3):
    flags.append(all(xs[i]))
for i in range(3):
    flags.append(all([xs[0][i], xs[1][i], xs[2][i]]))

flags.append(all([xs[0][0], xs[1][1], xs[2][2]]))
flags.append(all([xs[0][2], xs[1][1], xs[2][0]]))

if any(flags):
    print("Yes")
else:
    print("No")
