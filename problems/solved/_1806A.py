I, IN, M, R, LN, LS, P, S, ST, A = int, input, map, range, len, list, print, sum, str, abs
for _ in R(I(IN())):
    a, b, c, d = M(I, IN().split())
    u = d-b; r = c-a
    P("-1") if u < 0 or r > u else P(2*u-r)