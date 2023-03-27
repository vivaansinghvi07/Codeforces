I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min
I(IN()); p = LS(M(I, IN().split()))
a, b, c, d = M(p.count, [1, 2, 3, 4])
P(d + c + (b*2 + MX(0,a-c)+3)//4)