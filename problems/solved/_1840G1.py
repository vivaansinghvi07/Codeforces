cache = [False] * (1_000_001)
first = [0] * 1_000
dist = 0
for i in range(1_000):
    n = int(input())
    if cache[n] == True:
        print(f"! {dist - first.index(n)}", flush=True)
        exit()
    cache[n] = True
    first[i] = n
    dist += 1
    print("+ 1", flush=True)
for i in range(1_000):
    n = int(input())
    if cache[n] == True:
        print(f"! {dist - first.index(n)}", flush=True)
        exit()
    cache[n] = True
    dist += 1000
    print(f"+ 1000", flush=True)