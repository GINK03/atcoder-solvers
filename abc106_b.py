
b_size = {}
for b in range(1, int(input())+1):
  if b%2 == 0:
    continue
  size = len([by for by in range(1, b+1) if b%by == 0 and by%2 == 1])
  if size == 8:
    b_size[b] = size
print(len(b_size))

