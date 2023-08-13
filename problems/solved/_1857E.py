for _ in range(int(input())): 
	n, a = int(input()), sorted([*enumerate([*map(int, input().split())])], key=lambda x: x[1]) 
	d, s, c = [i[1]-j[1] for i, j in zip(a[1:], a)], [*range(n-1, 0, -1)], [0] * n
	x, y = 0, sum(dd*ss for dd, ss in zip(d, s)) + n	
	for i in range(n):
		c[a[i][0]] = x + y
		if i == n - 1: break
		y -= d[i] * s[i]
		x += (i+1) * d[i]
	print(*c)
