for _ in range(int(input())):
	n, a = int(input()), list(map(int, input().split()))
	p = min(a)+1
	for i in sorted(a)[1:]:
		p *= i
	print(p)
