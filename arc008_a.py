
N = int(input())

a = N%10 

n = N//10

m = min([n*100 + a*15, (n+1)*100])
print(m)
