I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
s = str(I(IN()) + 1)
while not (s[0] != s[1] and s[1] != s[2] and s[0] != s[2] and s[0] != s[3] and s[1] != s[3] and s[2] != s[3]):
    s = I(s)
    s += 1
    s = str(s)
P(s)
