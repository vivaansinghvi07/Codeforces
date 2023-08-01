for _ in range(int(input())):
    (_, c), s, fl, m, t = input().split(), input(), True, 0, 0
    if c == 'g': print(0); continue    
    for i, ch in enumerate(s*2):
        if fl and ch == c: fl = False; t = i
        elif not fl and ch == 'g': fl = True; m = max(m, i-t)
    print(m)