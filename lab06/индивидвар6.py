# variant.py
numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

selected = []
for number in numbers:
    if number % 3 == 0:
        selected.append(number)

sorted_copy = selected.copy()
sorted_copy.sort()

print(f"Список: {selected}")
print(f"Количество: {len(selected)}")
print(f"Сумма: {sum(selected)}")
print(f"Отсортированная копия: {sorted_copy}")
