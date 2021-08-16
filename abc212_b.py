
X = input()

if len(set(X)) == 1:
    print("Weak")
    exit()

X = list(map(int, X))


pn = 0
for i in range(3):
    if X[i+1] == (X[i] + 1)%10:
        pn += 1

if pn == 3:
    print("Weak")
    exit()
print("Strong")
