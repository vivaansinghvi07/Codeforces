print("\n".join([str(n-10**(len(str(n))-1)) for n in map(lambda x: int(x.strip()), [*open(0)][1:])]))
