n, m = map(int, input().split())
rows = [] 
for _ in range(n):
	row = set(input())
	if len(row) > 1:
		exit(print("NO"))
	rows.append(row.pop())
for (a, b) in zip(rows, rows[1::]):
	if a == b:
		exit(print("NO"))
print("YES") 
	
