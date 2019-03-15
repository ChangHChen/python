def palindromic_number_detector(number):
    trans = str(number)
    length = len(trans)
    if length == 5:
        if trans[0] == trans[length - 1] and trans[1] == trans[length - 2]:
            return "true"
        else:
            return "false"
    if length == 6:
        if trans[0] == trans[length - 1] and trans[1] == trans[length - 2] \
                and trans[2] == trans[length-3]:
            return "true"
        else:
            return "false"


max_palindromic_number = num1 = num2 = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        target_number = a * b
        if palindromic_number_detector(target_number) == "true" \
                and target_number > max_palindromic_number:
            max_palindromic_number = target_number
            num1 = a
            num2 = b

print(f"3桁の整数2つを掛けて得られる積が回文数となるもののうち最大の値は：\n"
      f"{max_palindromic_number} ({num1}*{num2})")
