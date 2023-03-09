I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
for _ in R(I(IN())):
    n = I(IN())
    if not n % 2:
        P("NO")
        continue
    j, k = n * 2 - (n // 2), n * 2
    P("YES")
    for i in R(1, n + 1): 
        if i % 2: 
            P(f"{i} {j}")
            j -= 1
        else:
            P(f"{i} {k}")
            k -= 1

