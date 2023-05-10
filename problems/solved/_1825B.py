I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    n, m = inp(); a = SO(inp())
    i, ii, j, jj = a[0], a[1], a[-1], a[-2]
    if ii - i > j - jj: P((n*m-MN(n, m))*(j-i)+(MN(n, m)-1)*(jj-i))
    else: P((n*m-MN(n, m))*(j-i)+(MN(n, m)-1)*(j-ii))