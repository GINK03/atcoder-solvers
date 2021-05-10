import re
 
s = input()
s = re.sub("0{1,}$", "", s)
 
 
if len(s)%2 == 0:
    sep = len(s)//2
    if list(s[:sep]) == list(reversed(s[sep:])):
        print("Yes")
    else:
        print("No")
 
else:
    mid = len(s)//2 + 1
    if list(s[:mid-1]) == list(reversed(s[mid:])):
        print("Yes")
    else:
        print("No")
