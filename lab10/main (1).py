
import os
from pathlib import Path
import files_lab
import table

def read_positive_integer():
    while True:
        user_input = input("Введите целое число > 0: ")
        try:
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Ошибка: число должно быть больше нуля.")
        except ValueError:
            print("Ошибка: нужно ввести целое число.")

def main():
    base_dir = Path(__file__).resolve().parent
    matrix_path = base_dir / "matrix.txt"
    report_path = base_dir / "report.txt"

    print("--- Задание 1: Надёжный ввод ---")
    print("Проверка read_positive_integer() (введите abc, 0, -2, 3):")
    size = read_positive_integer()
    print(f"Успешно введено: {size}\n")

    print("--- Задание 2 и 3: Чтение и отчет ---")
    try:
        # 1. Чтение и проверка матрицы (если ошибка - выброс исключения)
        matrix = files_lab.read_matrix(matrix_path)
        print("Матрица успешно прочитана:")
        for row in matrix:
            print(row)

        # 2. Вычисления
        r_sums = table.row_sums(matrix)
        c_sums = table.column_sums(matrix)
        variant_sum = files_lab.selected_sum(matrix)

        # 3. Формирование отчета
        report_content = (
            f"Суммы строк: {' '.join(map(str, r_sums))}\n"
            f"Суммы столбцов: {' '.join(map(str, c_sums))}\n"
            f"Результат варианта: {variant_sum}\n"
        )

        # 4. Запись отчета (ТОЛЬКО ПОСЛЕ УСПЕШНОЙ ПРОВЕРКИ)
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(report_content)
        
        print(f"\nОтчет успешно записан в {report_path}")
        print("Содержимое отчета:")
        print(report_content)

    except FileNotFoundError as e:
        print(f"Ошибка доступа: {e}")
        print("Отчет не был изменен.")
    except ValueError as e:
        print(f"Ошибка формата данных: {e}")
        print("Отчет не был изменен.")
    except OSError as e:
        print(f"Ошибка файловой системы: {e}")
        print("Отчет не был изменен.")

if __name__ == "__main__":
    main()
