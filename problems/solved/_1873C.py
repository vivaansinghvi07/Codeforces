for _ in range(int(input())):
    score = 0
    for i in range(10):
        if i > 4:
            max_score = 10 - i
        else:
            max_score = i + 1
        for j, c in enumerate(input()):
            if j > 4:
                temp_score = 10 - j
            else:
                temp_score = j + 1
            if c == 'X':
                score += min(max_score, temp_score)
    print(score)
