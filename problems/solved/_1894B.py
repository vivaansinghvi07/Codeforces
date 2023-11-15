from collections import Counter
for i in range(int(input())):
    b, mc, f, g = (n := int(input())) * [1], (c:=Counter(a:=[*map(int, input().split())])).most_common(2), True, True
    if not (2 <= len(c) <= n - 2 and mc[1][1] >= 2): print(-1)
    else: print(*[3 + (f:=False) if k == mc[0][0] and f else 2 + (g:=False) if k == mc[1][0] and g else 1 for k in a])
