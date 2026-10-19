numbers = input().split()

if len(numbers) == 0:
    print("Нет данных")
else:
    count = 0
    total = 0
    minimum = int(numbers[0])
    maximum = int(numbers[0])

    for item in numbers:
        number = int(item)
        count += 1
        total += number

        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

    average = total / count

    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", minimum)
    print("Максимум:", maximum)
    print("Среднее:", format(average, ".2f"))
