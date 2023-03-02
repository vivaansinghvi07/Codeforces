N, IN, R, LN = int, input, range, len
for _ in R(N(IN())):
    a, b = N(IN()), IN()
    c = ""
    for __ in R(a // 9 + 2):
        c += "FBFFBFFB"
    print("YES" if c.__contains__(b) else "NO")
