numbers = list(map(int, input().split()))

if len(numbers) == 0:
    print("Нет данных")
else:
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    positions = []

    for index, number in enumerate(numbers):
        if number == maximum:
            positions.append(index)

    print(positions)
