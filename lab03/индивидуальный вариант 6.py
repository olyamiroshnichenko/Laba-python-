
a = int(input("Введите загрузку процессора: "))

if a < 0 or a > 100:
    print("Ошибка диапазона")
elif a <= 29:
    print("Низкая")
elif a <= 69:
    print("Средняя")
else:
    print("Высокая")
