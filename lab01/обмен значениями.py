# swap.py

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print()
print("До обмена:")
print("first_room  =", first_room)
print("second_room =", second_room)

# Обмен значениями через третью переменную
temp = first_room
first_room = second_room
second_room = temp

print()
print("После обмена:")
print("first_room  =", first_room)
print("second_room =", second_room)
