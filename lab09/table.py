def row_sums(matrix):
    """Возвращает суммы элементов каждой строки."""
    result = []

    for row in matrix:
        result.append(sum(row))

    return result

def column_sums(matrix):
    """Возвращает суммы элементов каждого столбца."""
    if matrix == []:
        return []

    columns = len(matrix[0])
    result = []

    for column in range(columns):
        total = 0

        for row in matrix:
            total += row[column]

        result.append(total)

    return result

def diagonal_pattern(size):
    """Создаёт диагональный узор."""
    matrix = []

    for row in range(size):
        line = []

        for column in range(size):
            if row == column:
                line.append(0)
            elif row < column:
                line.append(1)
            else:
                line.append(2)

        matrix.append(line)

    return matrix

def main():
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))

    matrix = []

    for _ in range(rows):
        row = [int(part) for part in input("Введите строку: ").split()]

        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел.")
            row = [int(part) for part in input("Введите строку: ").split()]

        matrix.append(row)

    print("Матрица:")
    for row in matrix:
        print(*row)

    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    size = int(input("Введите размер диагонального узора: "))

    while size < 1:
        print("Размер должен быть положительным.")
        size = int(input("Введите размер диагонального узора: "))

    pattern = diagonal_pattern(size)

    print("Диагональный узор:")
    for row in pattern:
        print(*row)

if __name__ == "__main__":
    main()
