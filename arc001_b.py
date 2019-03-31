A, B = map(int, input().split())
Dorg = B - A
#print(Dorg)
mmm = []
for k10f in [0, 1]:
  for k05f in [0, 1]:
    D = Dorg
    k10 = D//10 + k10f
    D -= 10*k10
    k05 = D//5 + k05f
    D -= 5*k05
    k01 = D//1

    mmm.append(abs(k10) + abs(k05) + abs(k01))

print(min(mmm))
