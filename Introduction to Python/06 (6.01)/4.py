output = {"n": "○", "m": "●", "mn": "○●"}
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        key = "n"
    elif i % 5 == 0 and i % 3 != 0:
        key = "m"
    elif i % 3 == 0 and i % 5 == 0:
        key = "mn"
    else:
        key = i
        output[key] = key
    print(output[key])
