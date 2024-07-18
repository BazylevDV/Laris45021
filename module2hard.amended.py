n = int(input("Введите число от 3 до 20: "))
result = []

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)

result1 = ""
for p in result:
    result1 += str(p)

print(f"Пароль для числа {n}: {result1}")
