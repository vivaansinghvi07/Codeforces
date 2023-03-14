I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
n = I(IN())
if not n % 2:
    P(n // 2)
else:
    P(-(n//2+1))
