import sys
sys.setrecursionlimit(10**4)
for _ in range(int(input())):
	n = int(input())
	cache = [0] * (n+1)
	tree = [[0] * (n+1) for _ in range(n+1)]
	for _ in range(n-1):
		x, y = map(int, input().split())
		tree[x][y] = 1
		tree[y][x] = 1
	nums = [1]
	while len(nums) > 0:
		new = []
		for num in nums:
			for i in range(n+1):
				if tree[num][i]:
					tree[i][num] = 0
					new.append(i)
		nums = new
	def find_combinations(m: int) -> int:
		global tree, cache, n
		if c:=cache[m]: return c
		p = [i for i in range(n+1) if tree[m][i]]
		if len(p) == 0:
			return 1   # one spot where it can drop from
		a = 0
		for i in p:
			x = find_combinations(i)
			cache[i] = x
			a += x
		return a 
	for _ in range(int(input())):
		a, b = map(lambda x: find_combinations(int(x)), input().split())
		print(a*b)

