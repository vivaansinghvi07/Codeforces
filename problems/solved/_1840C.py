for _ in range(int(input())):
    [n, k, q], a = [[*map(int, input().split())] for _ in range(2)]
    b = list(map(lambda x: list(map(int, x.split())), " ".join([str(i) if i <= q else 'x' for i in a]).split('x')))
    print(sum([sum(range(1, len(s)+2-k)) for s in b]))