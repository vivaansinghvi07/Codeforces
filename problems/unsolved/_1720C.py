I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    r, c = inp()
    m = [LS(M(I, IN())) for _ in R(r)]
    s = S([S(a) for a in m])

    # look for: (assuming everything else is a 1)
    # 0 0   -- number is just the count of 1s
    # 1 1

    # 0 1   -- number is count of 1s
    # 1 0

    # 0 1   -- number is the count of 1s - 1
    # 1 1

    # 1 1   -- number is the count of 1s - 2
    # 1 1   

    if s == r * c - 1:
        P(s-1)
        continue
    elif s == r * c:
        P(s-2)
        continue

    ms = 5
    for rr in R(r):
        for cc in R(c):
            ss = 0
            try: ss += m[rr+1][cc] 
            except: ss += 1
            try: ss += m[rr-1][cc] 
            except: ss += 1
            try: ss += m[rr][cc+1] 
            except: ss += 1
            try: ss += m[rr][cc-1] 
            except: ss += 1
            ms = MN(ms, ss) if 0==m[rr][cc] else ms

    if ms < 4:
        P(s)
        continue

    f = False

    for rr in R(r):
        for cc in R(c):
            ss = m[rr][cc] == 0
            if not ss: break
            aa = 0
            for i in R(-1, 2, 2):
                for j in R(-1, 2, 2):
                    try: aa += m[cc+i][rr+j]
                    except: aa += 1
            f = aa < 4
            if f: break

    if f:
        P(s)
    else:
        P(s-1)
