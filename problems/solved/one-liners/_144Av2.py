n = int(input());a = list(map(int, input().split()));s = a.index(max(a)) + a[::-1].index(min(a));print(s-1 if s >= n else s)