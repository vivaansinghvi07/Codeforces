I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    r, c = inp()
    m = [LS(M(I, IN())) for _ in R(r)]
    s = S([S(a) for a in m])
    a = MN([S(m[i][j:j+2]) + S(m[i+1][j:j+2]) for j in R(c-1) for i in R(r-1)])
    P(s if a <= 2 else s - a + 2)