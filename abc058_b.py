
a = list(input())
b = list(input())
b.append("__DUMMY__")
c = sum(map(list, zip(a, b)), [])
print("".join(c).replace("__DUMMY__", ""))

