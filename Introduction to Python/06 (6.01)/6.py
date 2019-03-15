timec = {}
with open("workers.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        val = line.rstrip().split("\t")
        timec[val[0]] = int(val[1])
        print(f"{val[0]}：{timec[val[0]]:d}")
