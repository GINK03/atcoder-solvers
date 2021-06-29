
N = int(input())
S = [input() for _ in range(N)]

base = sum([s.count("AB") for s in S])
c1 = sum([s[0] == "B" and s[-1] == "A" for s in S])
c2 = sum([s[0] == "B" and s[-1] != "A" for s in S])
c3 = sum([s[0] != "B" and s[-1] == "A" for s in S])
c4 = sum([s[0] != "B" and s[-1] != "A" for s in S])

if c1 == c2 == c3 == 0:
    print(base)
elif c1 != 0 and c2 == c3 == 0:
    print(base + c1 - 1)
else:
    print(base + c1 + min(c2, c3))


