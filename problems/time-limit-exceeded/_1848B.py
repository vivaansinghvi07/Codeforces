for _ in range(int(input())):
    n, p = map(int, input().split())
    a = [*map(int, input().split())]
    m = [0] * (p+1)
    for i, v in enumerate(a + [None]):
        if i == n:
            for j in range(1, p+1):
                if m[j]:
                    m[j][1] += (i - m[j][0] - 1,)
        elif m[v] != 0:   
            m[v][1] += (i - m[v][0] - 1,)
            m[v][0] = i
        else:
            m[v] = [i, (i,)]
    print(min(map(lambda x: max(x[-2], x[-1] // 2), [sorted(x[1]) for x in m[1:] if x])))
        
