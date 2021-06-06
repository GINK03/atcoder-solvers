import re

S=input()

if re.search("^(dream|dreamer|erase|eraser){1,}$", S):
    print("YES")
else:
    print("NO")
