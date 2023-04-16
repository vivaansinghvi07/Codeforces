for _ in range(int(input())): 
    input()
    a = list(map(int, input().split()))
    c = {}
    for i in a:
        if not i in c:
            c[i] = 1
        else:
            c[i] += 1
    for k in c:
        if c[k] == 1:
            print(a.index(k) + 1)
