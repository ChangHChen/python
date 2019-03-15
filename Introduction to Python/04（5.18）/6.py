for row in range(10):
    if row == 0:
       row_ = 1
    elif row == 1:
        row_ = "spec"
    else:
        row_ = row
    for column in range(10):
        if row_ == "spec":
            if column == 1:
                print("+---", end="")
            else:
                print("-" * 4, end="")
        else:
            if column == 1:
                print("|", end="")
            else:
                if column == 0:
                    column += 1
            vol = column * row_
            if vol < 10:
                print("{:2d}".format(vol), " ", end="")
            else:
                print("{:1d}".format(vol), " ", end="")
    print("\n")