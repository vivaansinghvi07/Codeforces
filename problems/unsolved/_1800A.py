for _ in range (int(input())):
    n = int(input())
    s = input()
    letters = ['m', 'e', 'o', 'w']
    index = 0
    ans = "YES"
    for c in s:
        if c.toLower() == letters[index]:
            continue
        elif index == 3:
            ans = "NO"
            break
        elif c.toLower() == letters[index + 1]:
            index += 1
            continue
        else:
            ans = "NO"
            break
    print(ans)