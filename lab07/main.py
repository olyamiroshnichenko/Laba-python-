from functions import sum_digits, average, normalize_text, select_numbers

def main():
    number = int(input("Введите целое число: "))
    print("Сумма цифр:", sum_digits(number))

    line = input("Введите числа через пробел: ")
    numbers = [int(part) for part in line.split()]
    result = average(numbers)
    if result is None:
        print("Нет данных")
    else:
        print("Среднее:", result)

    threshold = int(input("Введите порог (целое неотрицательное число): "))
    print("Числа, равные порогу:", select_numbers(numbers, threshold))

    text = input("Введите произвольный текст: ")
    print("Нормализованный текст:", normalize_text(text))

if __name__ == "__main__":
    main()
