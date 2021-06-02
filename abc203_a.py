import collections
a,b,c=map(int,input().split())

dic = collections.Counter([a,b,c])

vk = {v:k for k,v in dic.items()}

if len(dic) == 3:
    print(0)
elif len(vk) == 1:
    print(vk[3])
else:
    print(vk[1])




