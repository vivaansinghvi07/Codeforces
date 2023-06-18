for _ in range(int(input())):
    n, m = map(int, input().split())
    p = [*range(n-2, -1, -2)] + [*range(n-1, -1, -2)]
    for i in p: print(*[m*i + j for j in range(1, m+1)])