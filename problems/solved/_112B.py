I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
n = IN()
f, s = 0, 0
for i in n:
    if i == "4":
        f += 1
    elif i == "7":
        s += 1
if s == 0 and f == 0:
    P("-1")
elif f >= s:
    P("4")
else:
    P("7")