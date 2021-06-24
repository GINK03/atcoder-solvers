

import timeit

def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print(f'"{function.__name__}" took {elapsed} seconds')
  return new_function

MOD = 10**9 + 7

""" mod combを用いるとテストケースで失敗する!! """
def mod_cmb(n, a, mod=MOD):
    nca = 1
    for i in range(a):
        nca *= (n - i) * pow(a - i, mod - 2, mod)
        nca %= mod
    return nca

N,M,K=map(int,input().split())
arg = [N,M,K]

# @timer
def main():
    N, M, K = arg
    h = N-(K+1)
    w = M+(K+1)

    path1 = mod_cmb(N+M, M)
    path2 = mod_cmb(h+w, w)

    if N > M + K:
        print(0)
    else:
        print(path1-path2)

if __name__ == "__main__":
    main()
