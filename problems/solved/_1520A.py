for _ in range(int(input())):
    input(); s = input(); temp = s[0]; uni = temp
    for c in s:
        if c == temp: continue
        uni += c; temp = c
    print("YNEOS"[len(uni) != len(set(uni))::2])