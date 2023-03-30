I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min
n, s = I(IN()), 0
for i in [100, 20, 10, 5, 1]:
    s += n // i
    n %= i
    if n == 0:
        break
print(s)