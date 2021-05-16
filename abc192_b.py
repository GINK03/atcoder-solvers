S=input()

a=[]
for i,s in enumerate(S):
    if i%2==0:
        if s==s.lower():
            ...
        else:
            print("No")
            exit(0)
    else:
        if s==s.upper():
            ...
        else:
            print("No")
            exit(0)
print("Yes")
        
