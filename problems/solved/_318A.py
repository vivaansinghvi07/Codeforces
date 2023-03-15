I, IN, M, R, LN, LS, P, S, ST = int, input, map, range, len, list, print, sum, str
n, k = M(I, IN().split())
if k <= -(-n//2):  
    P(k*2-1)
else:
    P(n-(n%2)-(n-k)*2)
