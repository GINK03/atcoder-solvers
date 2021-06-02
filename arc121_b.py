import collections
N = int(input())

ccount = collections.defaultdict(int)
kl = collections.defaultdict(list)
AC = []
for _ in range(2 * N):
    a, c = input().split()
    a = int(a)
    AC.append((a, c))
    ccount[c] += 1
    kl[c].append(a)
AC.sort()

for c in "RGB":
    ccount[c] %= 2

vcs = collections.defaultdict(list)
for c, v in ccount.items():
    vcs[v].append(kl[c])
if len(vcs[0]) == 3:
    print(0)
    exit()

def search_diff(lefts: list, rights: list) -> int:
    diff = float('inf')
    i = j = 0
    lefts.sort()
    rights.sort()
    while i < len(rights) and j < len(lefts):
        diff = min(diff, abs(lefts[j] - rights[i]))  # 距離を変更するにはここの実装を変える
        if rights[i] < lefts[j]:
            i += 1
        else:
            j += 1
    return diff

# all patterns
# 1. 奇数同士で消化する
# 2. 偶数奇数のペアで消化し合う
# print(vcs)
ans = min([search_diff(vcs[1][0], vcs[1][1]), search_diff(vcs[1][0], vcs[0][0]) + search_diff(vcs[1][1], vcs[0][0])])
print(ans)
