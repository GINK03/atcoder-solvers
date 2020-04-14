
import re

s = input()

ps = []
for p in re.findall('[A-Z][a-z]{0,}[A-Z]', s):
    ps.append(p)

ps = sorted(ps, key=lambda x:x.lower())
print(''.join(ps))


