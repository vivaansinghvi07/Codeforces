print("\n".join([str(max(a[1]*a[0], a[-1]*a[-2])) for a in [sorted(list(map(int, s.split()))) for s in [*open(0)][2::2]]]))