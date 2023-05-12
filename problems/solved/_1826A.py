for _ in range(int(input())):
    n = int(input()); a = [*map(int, input().split())]
    b = [0 for _ in range(n+1)]
    c = s = -1
    for i in a: b[i] += 1
    for i in b:
        c += 1
        n -= i
        s = c if n == c else s
    print(s)