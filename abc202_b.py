
S=input()

R={'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

x = [R[c] for c in reversed(S)]
print(''.join(x))

