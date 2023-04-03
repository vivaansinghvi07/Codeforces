I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
s, n = inp(); a = "YES"
for t, g in SO([inp() for _ in R(n)]):
    if s > t: s += g
    else: a = "NO"
P(a)