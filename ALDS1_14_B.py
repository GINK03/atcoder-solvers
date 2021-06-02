
s0 = input()
s1 = input()

'''
ret = -1
while True:
    ret = s0.find(s1, ret + 1)
    if ret == -1:
        break
    print(ret)
'''

size = len(s1)
for i0 in range(len(s0) - size + 1):
    if s0[i0:i0+size] == s1:
        print(i0)
    
