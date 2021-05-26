
# https://colab.research.google.com/drive/1eMsF-ktVhngc8Izci2GwFBPK49lTo0Op?usp=sharing
s=input()
tmp = ''
N = len(s)
acc = 0
for i in range(len(s)):
    if s[i] == 'W':
        acc += i - len(tmp)
        tmp += 'W'
print(acc)
