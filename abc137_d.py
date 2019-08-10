N,M=map(int,input().split())

xs = []
for n in range(N):
    a,b = map(int,input().split())
    xs.append((a,b))

def obj(x):
    return (x[1])*-1
xs = sorted(xs,key=lambda x:obj(x))
print(xs)

day_exs = {}
for day, pay in xs:
    if day_exs.get(day) is None:
        day_exs[day] = []
    day_exs[day].append(pay)
print(day_exs)

