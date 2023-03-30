I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
n, m = inp(); a = SO(inp()); s = a[-1]-a[0]
for i in R(m-n+1): s = MN(s, MX(a[i:i+n]) - MN(a[i:i+n]))
P(s)