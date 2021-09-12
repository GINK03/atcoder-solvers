
s = set("ABC,ARC,AGC,AHC".split(","))

t = {input() for i in range(3)}

print(list(s-t)[0])
