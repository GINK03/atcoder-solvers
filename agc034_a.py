
N, A, B, C, D = map(int, input().split())
S = input()
A -= 1
B -= 1
C -= 1
D -= 1
if "##" in S[A:max(C, D)]:
  print("No")
  exit()
if C<D:
  print("Yes")
else:
  if "..." in S[B-1:D+2]:
    print("Yes")
  else:
    print("No")
