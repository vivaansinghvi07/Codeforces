print("\n".join(["1" if n==1 else "-1" if n%2 else " ".join([str(i+((i%2==1)*2-1)) for i in range(1, n+1)]) for n in map(int, [*open(0)][1::])]))