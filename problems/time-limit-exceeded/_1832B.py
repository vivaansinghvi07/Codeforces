I = lambda: list(map(int, input().split()))
for _ in range(int(input())):
    n, k = I(); a = sorted(I())
    print(max([sum(a[2*i:n-(k-i)]) for i in range(k+1)]))