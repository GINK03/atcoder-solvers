x = int(input())

c500 = x // 500
x %= 500
c005 = x // 5

print(c500 * 1000 + c005 * 5)
