I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
a,b=inp()
for i in R(a):
    for j in R(b):
        P("#" if not i % 2 or j == 0 and i % 4 == 3 or j == b-1 and i % 4 == 1 else ".", end="")
    P()