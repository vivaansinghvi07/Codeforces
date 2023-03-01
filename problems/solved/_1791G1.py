# unreadable code >>

I, N, M, R, L, LS = int, input, map, range, len, list
for _ in R(I(N())):
    a, b = M(I, N().split(" "))
    c = LS(M(I, N().split(" ")))
    d = []
    for i in R(L(c)):
        d.append(c[i] + i + 1)
    d.sort()
    m = 0
    while b >= 0:
        try:
            b -= d[m]
        except:
            m = L(c) + 1
            break
        m += 1
    print(m-1)