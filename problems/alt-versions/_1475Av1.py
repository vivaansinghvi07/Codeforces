import math
I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    n = I(IN()); print(["YES", "NO"][math.log2(n) % 1 == 0])