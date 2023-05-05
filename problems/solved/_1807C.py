alphabet = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())): 
    n = int(input()); 
    s = input(); 
    d = {c: 0 for c in alphabet}
    ans = "YES"
    for i in range(n):
        c = s[i]
        if d[c]: 
            if d[c] != i % 2 + 1:
                ans = "NO"
        else:
            d[c] = i % 2 + 1
    print(ans)