IN = input
a, b = IN(), IN()
c = sum(map(int, b.split(" ")))
print ("EASY" if c == 0 else "HARD")