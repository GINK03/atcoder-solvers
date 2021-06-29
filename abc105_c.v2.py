
N=int(input())

def decimal_to_base(x: int, base: int) -> list:
    if x//base:
        return decimal_to_base(x//base, base) + [x%base]
    return [x%base]
 
arr = decimal_to_base(-1 * N, -2)
print(*[abs(x) for x in arr], sep="")
