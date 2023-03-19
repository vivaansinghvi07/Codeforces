I, IN, M, R, LN, LS, P, S, ST, A = int, input, map, range, len, list, print, sum, str, abs
n = I(IN())
for i in R(n): a = "love" if i % 2 else "hate"; t = "that" if i != n-1 else "it"; P(f"I {a} {t}", end=" ")