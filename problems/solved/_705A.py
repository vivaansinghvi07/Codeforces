I, IN, M, R, LN, LS, P, S, ST = int, input, map, range, len, list, print, sum, str
n = I(IN())
for i in R(n-1):
    a = "hate" if not i % 2 else "love"
    P(f"I {a} that", end = " ")
a = "hate" if n % 2 else "love"
P(f"I {a} it")
