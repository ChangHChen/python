# 　数学的な作法でやってみた、ランニング時間が正常になった
prime_number = {}
target_number = 1


# 　ある整数のすべての因数を求める関数
def factorization(number):
    prime_number_temp = {}
    num = 2  # すべての整数が１の倍数になるので、２から試みる
    while num < number + 1:
        if number % num == 0:
            if num in prime_number_temp.keys():
                prime_number_temp[num] += 1
            else:
                prime_number_temp[num] = 1
            number /= num
        else:
            num += 1
    for num in prime_number_temp.keys():
        if num not in prime_number.keys():
            prime_number[num] = prime_number_temp[num]
        else:
            # xのすべでの因数がある整数の因数に含まれている場合、
            # ｘは必ずその整数で割り切れるため、重なり入れる必要がない
            if prime_number[num] < prime_number_temp[num]:
                prime_number[num] = prime_number_temp[num]


for x in range(1, 21):
    factorization(x)
for p_number in prime_number.keys():
    for times in range(prime_number[p_number]):
        target_number *= p_number

print("**数学的な方法**")
print(f"1から20までのすべての整数で割りきれる最小の数は：{target_number}")
