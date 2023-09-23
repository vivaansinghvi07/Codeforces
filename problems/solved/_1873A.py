print("\n".join(["YNEOS"[sum([int(r!=t) for r, t in zip('abc', s.strip())])>2::2] for s in [*open(0)][1::]]))
