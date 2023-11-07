n, a = int(input()), input().split()

"""
plan:

Since we can have numbers whose lengths are more than others, a map storing the difference, depending on the length of the second number.

If a number is 12345, we store:
{1: 3+4+5-(1+2), 2: None, 3: 2+3+4+5-(1), 4: None, 5: (1+2+3+4+5)}
In the form: 
{length_of_target: required_value_of_target}

We also do something similar for the beginning of each thing.
{1: (1+2+3)-(4+5) ...}

If the number is 12, we store:

{1|3|5: None, 2: 1+2, 4: 1+2 - ...}   Here, we can simply compute the new length 

Let's do this:

If the number is 123
{1: "(2+3-1)", 2: None, 3: "(1+2+3)", 4: None, 5: "!3"}  where "3" is the length of the thing 

this number right here is in fact the sum that the following works with: 
when the other number is 12345
1+2+3+4-5

12 + another number
12 + 3321 works, but 12 + 6333 also works

"""

e1, e2, e3 = {3:{},5:{}},{4:{}},{5:{}}

he = [{} for _ in range(5)]
for x in a:
    d = len(x)
    if d == 5:
        for j in range(1, 6, 2):
            c = 2 - j // 2
            y = sum(map(int, x[c:])) - sum(map(int, x[:c]))
            he[j-1][y] = he[j-1].get(y, 0) + 1 
    elif d == 4:
        for j in range(2, 5, 2):
            c = int(j == 2)
            y = sum(map(int, x[c:])) - sum(map(int, x[:c]))
            he[j-1][y] = he[j-1].get(y, 0) + 1
    elif d == 3:
        for j in range(1, 4, 2):
            c = int(j == 1)
            y = sum(map(int, x[c:])) - sum(map(int, x[:c]))
            he[j-1][y] = he[j-1].get(y, 0) + 1
        e3[5][y] = e3[5].get(y, 0) + 1 
    elif d == 2:
        y = sum(map(int, x))
        he[2-1][y] = he[2-1].get(y, 0) + 1 
        e2[4][y] = e2[4].get(y, 0) + 1 
    elif d == 1:
        y = int(x)
        he[0][y] = he[0].get(y, 0) + 1 
        e1[3][y] = e1[3].get(y, 0) + 1
        e1[5][y] = e1[5].get(y, 0) + 1

o = 0
for x in a:
    d = len(x)
    if d == 1 or d == 2:
        y = sum(map(int, x))
        o += he[d-1].get(y, 0)
    if d == 3:
        y = sum(map(int, x))
        o += he[d-1].get(y, 0)
        y = sum(map(int, x[:-1])) - int(x[-1])
        o += e1[3].get(y, 0)
    if d == 4:
        y = sum(map(int, x))
        o += he[d-1].get(y, 0)
        y = sum(map(int, x[:-1])) - int(x[-1])
        o += e2[4].get(y, 0)
    if d == 5:
        y = sum(map(int, x))
        o += he[d-1].get(y, 0)
        y = sum(map(int, x[:-1])) - int(x[-1])
        o += e3[5].get(y, 0)
        y = sum(map(int, x[:-2])) - sum(map(int, x[-2:]))
        o += e1[5].get(y, 0)

print(o)













