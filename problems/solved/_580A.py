a = int(input())
m = list(map(int, input().split()))
s = h = x = 0
for i in m: 
    if i >= h: s += 1
    else: x = max(s, x); s = 1
    h = i
print(max(s,x))