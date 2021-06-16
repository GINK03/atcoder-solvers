def main():
    N, K = map(int, input().split())
    S = list(input())
    T = list(S)

    for i in range(N):
        a = T[i]
        i1 = i
        k_needed_1 = 0
        for j in range(i + 1, N):
            if a > T[j]:
                k_needed = 0
                if S[i] != T[j]:
                    k_needed += 1
                if S[j] != T[i]:
                    k_needed += 1
                if S[i] != T[i]:
                    k_needed -= 1
                if S[j] != T[j]:
                    k_needed -= 1

                if K >= k_needed:
                    a = T[j]
                    i1 = j
                    k_needed_1 = k_needed
        if i1 != i:
            T[i], T[i1] = T[i1], T[i]
            K -= k_needed_1

    print(*T, sep="")


if __name__ == '__main__':
    main()
