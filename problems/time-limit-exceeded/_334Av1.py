I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
s = 1
a = "".join([IN() for _ in R(I(IN()))])
P(a.count("00") + a.count("11") + 1)