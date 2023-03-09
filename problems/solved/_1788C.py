I, IN, M, R, LN, LS, P = int, input, map, range, len, list, print
for _ in R(I(IN())):
    n = I(IN())
    a = [i for i in R(1, n * 2 + 1)]
    if not n % 2:
        P("NO")
        continue
    j, k = LN(a) - 1 - (n // 2), LN(a) - 1
    P("YES")
    for i in R(n): 
        if not i % 2: 
            P(f"{a[i]} {a[j]}")
            j -= 1
        else:
            P(f"{a[i]} {a[k]}")
            k -= 1

