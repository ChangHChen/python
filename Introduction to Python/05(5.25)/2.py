with open("data0501.txt", mode="r", encoding="utf-8") as f:
    total = 0
    for data in f:
        print(int(data))
        total += int(data)

print("\ntotal value =", total)
