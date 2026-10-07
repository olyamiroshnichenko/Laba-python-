#minimum.py
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and a <= c:
    print("Минимальное число:", a)
elif b <= a and b <= c:
    print("Минимальное число:", b)
else:
    print("Минимальное число:", c)
