import re; ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; import math
def n(s: str): return sum([(ALPHABET.index(c)+1)*26**(len(s)-i-1) for i, c in enumerate(s)])
def m(n: int): return "".join([(" "+ALPHABET)[(n%(26**(i+1)))//26**i] for i in range(math.ceil(math.log(n, 26)), -1, -1)]).strip()
def a(s: str): return f"R{''.join([c for c in s if c.isnumeric()])}C{str(n([c for c in s if c.isalpha()]))}"
def b(s: str): r, c = re.split(r"[A-Z]+", s)[1::]; return f"{m(int(c))}{r}"
for _ in range(int(input())): s = input(); print(b(s) if re.match(r"R[0-9]+C[0-9]+", s) else a(s))