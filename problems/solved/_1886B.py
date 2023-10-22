import math
for i in range(int(input())):
    (p, a, b), o = [list(map(int, input().split())) for _ in range(3)], [0, 0]
    oa, ob, pa, pb, ab = math.dist(o, a), math.dist(o, b), math.dist(p, a), math.dist(p, b), math.dist(a, b)
    print(min(max(pa, ob, ab/2), max(pb, oa, ab/2), max(ob, pb), max(oa, pa)))
