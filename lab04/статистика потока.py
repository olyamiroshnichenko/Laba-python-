n = int(input("Введите количество чисел: "))

total = 0
positive = 0

first = int(input("Введите число: "))
total += first

if first > 0:
    positive += 1

maximum = first

for i in range(n - 1):
    number = int(input("Введите число: "))
    total += number

    if number > 0:
        positive += 1

    if number > maximum:
        maximum = number

print("Сумма:", total)
print("Положительных:", positive)
print("Максимум:", maximum)
