
import sys
import logging
 
 
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True) + [0]
 
    def cumsum(x):
        return x * (x + 1) // 2
 
    k_remaining = k
    ans = 0
    for i in range(n):
        if a[i] == a[i + 1]:
            continue
 
        if k_remaining >= (i + 1) * (a[i] - a[i + 1]):
            ans += (cumsum(a[i]) - cumsum(a[i + 1])) * (i + 1)
            k_remaining -= (i + 1) * (a[i] - a[i + 1])
        else:
            j = k_remaining // (i + 1)
            r = k_remaining % (i + 1)
            logging.debug((j, r))
            ans += (cumsum(a[i]) - cumsum(a[i] - j)) * (i + 1)
            ans += (a[i] - j) * r
            k_remaining = 0
 
        if k_remaining == 0:
            break
 
    print(ans)
 
 
if __name__ == "__main__":
    loglevel = "DEBUG" if "--debug" in sys.argv else "WARNING"
    numeric_level = getattr(logging, loglevel, None)
    log_format = "%(levelname)s (%(asctime)s.%(msecs)d): %(message)s"
    logging.basicConfig(level=numeric_level, format=log_format, datefmt="%I:%M:%S")
 
    main()
