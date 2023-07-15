s = input(); a = [0] * 4; b = [0] * 4
for i, c in enumerate(s):
	if c == '!': continue
	a[i%4] = c
for i, c in enumerate(s):
	if c != '!': continue
	b[['R', 'B', 'Y', 'G'].index(a[i%4])] += 1
print(*b)
