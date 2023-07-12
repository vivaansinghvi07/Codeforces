w = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
def f(b):
	for i in w:
		if b[i[0]//3][i[0]%3] == b[i[1]//3][i[1]%3] == (a:=b[i[2]//3][i[2]%3]) != '.':
			print(a); return 
	print('DRAW')
for _ in range(int(input())):
	f([[*input()] for _ in range(3)])