with open("workers.txt", mode="a", encoding="utf-8") as f:
    dict = {}
    print(f"***名前に”END”を入力したら、終了する***")
    while True:
        name = str(input("名前を入力してください："))
        if name == "END":
            break
        time = int(input("勤務時間を入力してください："))

        if name not in dict.keys():
            dict[name] = time
        else:
            dict[name] += time
    for n in dict.keys():
        s = f"{n}\t{dict[n]}\n"
        f.write(s)
