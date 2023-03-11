import math
I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
n = I(IN())
a = M(I, IN().split(" "))
a = sorted(a, reverse = True)
c = 0
t = 0
s = sum(a)
for i in a:
    t += i
    c += 1
    if t > s // 2:
        break
P(c)
