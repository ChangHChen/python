dict = {0: [1, 2, 3, 4, 5], 1: ["浅草", "清水寺", "立川", "丸山"],
        2: ["red", "brown", "yellow"]}
for n in dict.keys():
    temp = []
    for i in range(len(dict[n])):
        s = len(dict[n]) - i - 1
        temp.append(dict[n][s])
    print(f"{dict[n]}\t==>{temp}")
