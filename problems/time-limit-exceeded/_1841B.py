for _ in range(int(input())):
    n = int(input()); a = list(map(int, input().split()))
    s = False; o = ''; t = -1
    for i in a:
        if not s:
            if i < t: 
                if i > a[0]:
                    o += '0'
                else:
                    t = i; s = True; o += '1'
            else: t = i; o += '1'
        elif i >= t and i <= a[0]: t = i; o += '1'
        else: o += '0'
    print(o)
