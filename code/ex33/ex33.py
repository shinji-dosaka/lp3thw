i = 0
numbers = []

while i < 6:
    print(f"ループの先頭でiは{i}")
    numbers.append(i)

    i = i + 1
    print("numbersリスト:", numbers)
    print(f"ループの末尾でiは{i}")


print("numbersリスト:")

for num in numbers:
    print(num)
