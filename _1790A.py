print("\n".join([str(sum([1 for i in range(len(x)) if "314159265358979323846264338327"[:i+1] == x[:i+1]])) for x in map(lambda x: str(x).strip(), [*open(0)][1::])]))
