s = input()
ans   = 0
stack = [0]
for c in s:
  if c == '(':
    stack.append(0)
  else:
    if len(stack) == 1:
      stack[0] = 0
      continue
    stack.pop()
    stack[-1] += 1
    ans += stack[-1]
print(ans)
