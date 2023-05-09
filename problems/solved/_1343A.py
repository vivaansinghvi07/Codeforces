I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
G = [2**n-1 for n in R(2, 50)]
for _ in R(I(IN())):
    n = I(IN())
    for i in G:
        if not n % i:
            P(n // i)
            break