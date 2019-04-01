N = input()

vs = [int(x) for x in input().split()]
cs = [int(x) for x in input().split()]

m = sum([v-c for v,c in zip(vs,cs) if v-c > 0])
print(m)

