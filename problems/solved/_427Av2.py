I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
n, a, s, m = I(IN()), inp(), 0, 0
for i in a: s += i; m = MN(m, s)
P(A(m))