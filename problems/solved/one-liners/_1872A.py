print("\n".join([str(int(-(-abs((a-b)/2)//c))) for a, b, c in map(lambda x: map(int, x.split()), [*open(0)][1:])]))