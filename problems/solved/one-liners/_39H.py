def to_base(n, b):
    from math import log, ceil; p = ceil(log(n, b)); o = ''
    while p > -1: x=n//(b**p); n-=(b**p)*x; o+=str(x); p-=1
    return o if o[0] != '0' else o[1:]
n = int(input()); print("\n".join([" ".join([to_base(j*i, n) for j in range(1, n)]) for i in range(1, n)]));