
S = int(input())

# x_1 * y_2 - x_2 * y_1 = S
# ->  x_1 - 10**9 * y_1 = S
x3, y3 = 0, 0
x2, y2 = 10**9, 1

V  = 10**9
x1 = (V-S%(V))%V
y1 = (S+x1)//V
print(x3, y3, x2, y2, x1, y1)
