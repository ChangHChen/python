dict = {0: [1, 1, 1, 1, 1], 1: [1, 1, 1, 1, 1, 0], 2: [-1, -1, -1, -1],
        3: ["abc", "abc", "abc"], 4: [5, 5, 5, 4, 5]}
for m in dict.keys():
    print(f"{dict[m]}\t==>", end=" ")
    first = dict[m][0]
    result = "True"
    for n in range(1, len(dict[m])):
        if dict[m][n] != first:
            result = "False"
    print(result)
