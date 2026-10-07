#variant.py
total = int(input("Введите количество файлов: "))
capacity = int(input("Введите вместимость каталога: "))

full_units = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity

print("Полностью заполненных каталогов:", full_units)
print("Остаток файлов:", remainder)
print("Минимальное количество каталогов:", min_units)
