N=int(input())

def dfs(lst):
    if len(lst) == N:
        print("".join(lst))
        return

    for ci in range(ord("a"), ord(max(lst))+1+1):
        dfs(lst[:] + [chr(ci)])



dfs(["a"])



