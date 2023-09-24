for _ in range(int(input())):
    (n, k), (s, p), a, l = map(int, input().split()), (0, 0), input(), False
    for i, c in enumerate(a):
        if c == 'B':
            if not l or (i - p) >= k:
                p = i
                s += 1
                if not l:
                    l = True
                    continue
    print(s)
