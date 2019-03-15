total = 0
numbers = []
for i in range(1, 1001):
    if i % 3 == 2 and i % 4 == 1:
        numbers.append(i)
        total += i
print(f"条件を満たす整数は{numbers}です\n合計は{total:d}です")
