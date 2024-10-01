def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)

    return result
n = int(input("Введите число n: "))
password = generate_password(n)
print(f"Пароль для числа {n}: {password}")
