I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min
a = []
for _ in R(4): a.append(I(IN()))
c = [0 for _ in R(I(IN()))]
for i in a: 
    for x in R(i-1, LN(c), i): c[x] = 1
P(S(c))