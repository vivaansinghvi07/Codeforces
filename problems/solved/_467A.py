I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
c = 0
for _ in R(I(IN())):
    s, p = M(I, IN().split(" "))
    if not s + 2 > p:
        c += 1
P(c)