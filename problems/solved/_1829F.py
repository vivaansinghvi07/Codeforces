for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0 for _ in range(n+1)]
    for _ in range(m):
        i, j = map(int, input().split())
        a[i] += 1; a[j] += 1
    print(m-(y:=a.count(1)), y//(m-y))