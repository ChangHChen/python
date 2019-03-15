for i in range(9):
    if i < 5:
        op = "#" * (i + 1)
    else:
        op = "#" * (9 - i)
    print(op)
