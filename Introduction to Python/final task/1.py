all_group = []
group = []

for x in range(1, 16):
    for y in range(x, 16):
        for z in range (y, 16):
            if x + y + z == 16:
                group = [x, y, z]
                all_group.append(group)

print(f"3つの自然数の合計が16になるような組み合わせは")
for i in range(len(all_group)):
    print(f"{all_group[i]}")
