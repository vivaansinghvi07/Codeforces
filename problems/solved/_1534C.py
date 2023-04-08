I, IN, M, R, LN, LS, P, S, ST, A, SO, MX, MN = int, input, map, range, len, list, print, sum, str, abs, sorted, max, min; inp = lambda: LS(M(I, IN().split()))
for _ in R(I(IN())):
    n = I(IN()); a, b = inp(), inp(); c = [-1 for _ in R(n)]; d = [False for _ in R(n)]
    for i in R(n): c[a[i]-1] = b[i]-1
    s = 0
    for i in R(n): 
        b = True; ii = i
        if d[i]: continue
        while True: 
            d[ii] = True
            ii = c[ii]
            if d[ii]:
                s+=1
                break
    P(pow(2, s, 10**9+7))