I, IN, M, R, LN, LS, P, S, ST, A = int, input, map, range, len, list, print, sum, str, abs
a, b, c = I(IN()), I(IN()), I(IN())
P(max(a*b*c, (a+b)*c, a+b+c, a*(b+c)))