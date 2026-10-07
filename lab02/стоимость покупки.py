#purchase.py

price = int(input("Введите цену одной тетради: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму: "))

cost = price * count
change = paid - cost

print("Стоимость:", cost)
print("Сдача:", change)
