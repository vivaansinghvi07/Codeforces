from collections import Counter
inp = lambda: list(map(int, input().split()))
for _ in range(int(input())):
	n = int(input())
	a = Counter(inp())
	print('- 0', flush=True)
	b = Counter(arr:=inp())
	if a == b:
		print('- 0', flush=True)
		b = Counter(arr:=inp())
	dif = [*(b-a)][0]
	r = []
	for i, j in enumerate(arr):
		if j == dif:
			continue
		r.append(i+1)
	print('-', len(r), *r, flush=True)
	c = inp()
	if (len(c)) == 1:
		print('! 1', flush=True)
		continue
	if len({*Counter(c)}) == 1:
		print('- 0', flush=True)
		c = inp()
	print('!', c.index(({*Counter(c)}-{dif}).pop())+1, flush=True)