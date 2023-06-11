inp = lambda: list(map(int, input().split()))
ele = lambda x: x[1]
for _ in range(int(input())):
    [n, k], a, b = inp(), sorted(enumerate(inp()), key=ele), sorted(inp())
    c = [0] * n
    for i in range(n): c[a[i][0]] = b[i]
    print(*c)
