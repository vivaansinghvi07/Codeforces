I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
def solve():
    n = I(IN())
    for i in [4, 7, 47, 447, 477, 747, 777]:
        if not n % i:
            print("YES")
            return
    print("NO")
solve()