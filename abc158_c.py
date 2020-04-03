A,B = map(lambda x:int(x), input().split())

x_s = int(50*(A+B)/9) 
x_e = int(50*(A+B+1)/9) 
a = -1
for x in range(x_s, x_e+1):
    if int(x*0.08) == A and int(x*0.1) == B:
        a = x
        break
print(a)
