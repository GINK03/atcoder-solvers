
A, B = map(int, input().split())

slice = sorted([A, A-1, B, B-1])[-2:]
print(sum(slice))
