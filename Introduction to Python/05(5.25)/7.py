with open("data0502.txt", mode="r", encoding="utf-8") as f:
    for data in f:
        val = data.split(",")
        a = 0
        for i in val:
            if int(i) > a:
                a = int(i)
        print(a)
