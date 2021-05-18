N=int(input())


state = []
for _ in range(N):
    w = int(input())

    is_ok = False
    for i in range(len(state)):
        if state[i][-1] >= w:
            state[i].append(w)
            is_ok = True
            break

    if is_ok is False:
        state.append([w])

print(len(state))
