for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [[*input()] for _ in range(n)]
    s = [{a[i][j] for i in range(n)} for j in range(m)]
    l, b, a = 'vika', 0, "NO"
    for j in range(m):
        if l[b] in s[j]:
            if (b:=b+1) == 4:
                a = "YES"
                break
    print(a)