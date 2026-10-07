count = 0

number = int(input("Введите положительное число: "))

while number <= 0:
    count += 1
    number = int(input("Введите положительное число: "))

print("Квадрат:", number ** 2)
print("Количество отклонённых попыток:", count)
