I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
s = -1
t = 2
for mag in open(0):
    if t != mag:
        t = mag
        s += 1
P(s)