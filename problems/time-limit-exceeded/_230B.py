n = int(input()); a = list(map(int, input().split())); d = ["YES" if not a[i]**0.5 % 1 and (sum([not int(a[i]**0.5) % a for a in range(2, int(a[i]**0.5))])==0 if int(a[i]**0.5) != 1 else False) else "NO" for i in range(n)]; print("\n".join(d))