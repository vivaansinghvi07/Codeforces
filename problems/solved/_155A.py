I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
n, a, s, mx, mn = I(IN()), inp(), 0, 0, 10000
for l in R(n): i = a[l]; s += (i > mx or i < mn) and l != 0; mx = MX(mx, i); mn = MN(mn, i); P(s) if l == n-1 else 0