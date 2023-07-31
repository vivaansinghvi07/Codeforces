for _ in range(int(input())):
	n, k = map(int, input().split())
	print(min(n+1, 2**(min(k, 30))))