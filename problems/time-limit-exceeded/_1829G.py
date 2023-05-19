m = [n*(n+1)//2 for n in range(1, 1416)]
for _ in range(int(input())):
    n = int(input()); d = 0; a = [n] 
    if n == 1: print(1); continue
    for i in range(len(m)): 
        if n <= m[i]: d = i; break
    i, j = m[d-1]+1, m[d]; d -= 1
    l = n-i-1; r = j-n-1
    while l>0 or r>0:
        a.extend([*range(m[d-1]+1+max(l, 0), m[d]-max(r, 0)+1)])
        d -= 1; l -= 1; r -= 1
    a.extend([*range(1, m[d]+1)])
    print(sum(map(lambda x: x*x, a)))