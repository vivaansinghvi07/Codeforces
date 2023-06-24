""" Max recursive depth was reached - increasing this breaks the memory limit. """
import sys; sys.setrecursionlimit(100000)
s = 0; t = 0; a = []; p = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def solve(a, r, x, y):
    global t, s
    try:
        if not a[x][y] or x<0 or y<0: return
        else: t += a[x][y]; a[x][y] = 0
    except: return
    for xx, yy in p: solve(a, False, x+xx, y+yy)
    if r: s = max(s, t); t = 0  
for _ in range(int(input())):
    n, m, s = *map(int, input().split()), 0
    a = [list(map(int, input().split())) for _ in range(n)]
    for x in range(n):
        for y in range(m): solve(a, True, x, y)
    print(s)
