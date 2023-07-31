print("\n".join([str(max(0, min([i-j for i, j in zip(a[1:], a)])//2+1)) for a in map(lambda x: [*map(int, x.split())], [*open(0)][2::2])]))
