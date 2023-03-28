I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min
a = LS(M(I, " ".join([IN() for _ in R(I(IN()))]).split())); h, g = a[::2], a[1::2]
P(S([hh==gg for gg in g for hh in h]))