def read_matrix(path):
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {path} не найден.")
    except UnicodeDecodeError:
        raise ValueError("Ошибка кодировки файла. Ожидается UTF-8.")

    while lines and not lines[-1].strip():
        lines.pop()

    if not lines:
        raise ValueError("Файл пуст.")

    # 1. Парсинг заголовка
    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось два числа (количество строк и столбцов).")
    
    try:
        rows = int(header[0])
        cols = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами.")
    
    if rows <= 0 or cols <= 0:
        raise ValueError("Строка 1: размеры матрицы должны быть положительными.")

    # 2. Проверка количества строк
    data_lines = lines[1:]
    if len(data_lines) != rows:
        raise ValueError(f"Ожидалось {rows} строк данных, получено {len(data_lines)}.")

    # 3. Парсинг данных
    matrix = []
    for i, line in enumerate(data_lines):
        line_num = i + 2  # Номер строки в файле (с учетом заголовка)
        parts = line.split()
        
        if len(parts) != cols:
            raise ValueError(f"Строка {line_num}: ожидалось {cols} чисел, получено {len(parts)}.")
        
        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(f"Строка {line_num}: '{part}' не является целым числом.")
        matrix.append(row)
    
    return matrix


def selected_sum(matrix):
    
#Индивидуальный вариант 2: Сумма отрицательных элементов.
    
    total = 0
    for row in matrix:
        for item in row:
            if item < 0:
                total += item
    return total
