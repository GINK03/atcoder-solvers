
S = input()

head, tail = int(S[0:2]), int(S[2:4])

if 1 <= head <= 12 and 1<= tail <= 12:
    print('AMBIGUOUS')
elif 1<=head<=12 and 0<=tail<=99:
    print('MMYY')
elif 0<=head<=99 and 1<=tail<=12:
    print('YYMM')
else:
    print('NA')


