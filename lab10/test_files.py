
from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

def test_read_matrix():
    with TemporaryDirectory() as directory:
        dir_path = Path(directory)
        
        # 1. Успешное чтение
        p1 = dir_path / "m1.txt"
        p1.write_text("1 2\n7 -1\n", encoding="utf-8")
        assert read_matrix(p1) == [[7, -1]]
        
        # 2. Матрица 1x1
        p2 = dir_path / "m2.txt"
        p2.write_text("1 1\n0\n", encoding="utf-8")
        assert read_matrix(p2) == [[0]]

        # 3. Пустой файл
        p3 = dir_path / "m3.txt"
        p3.write_text("", encoding="utf-8")
        try:
            read_matrix(p3)
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена: пустой файл"

        # 4. Заголовок 0 3
        p4 = dir_path / "m4.txt"
        p4.write_text("0 3\n1 2 3\n", encoding="utf-8")
        try:
            read_matrix(p4)
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена: нулевой размер"

        # 5. Неверное количество чисел в строке
        p5 = dir_path / "m5.txt"
        p5.write_text("1 2\n1\n", encoding="utf-8")
        try:
            read_matrix(p5)
        except ValueError as e:
            assert "Строка 2" in str(e), "Ошибка должна указывать на строку 2"
        else:
            assert False, "Ошибка не обнаружена: мало чисел в строке"

        # 6. Нечисловая ячейка
        p6 = dir_path / "m6.txt"
        p6.write_text("1 2\n1 x\n", encoding="utf-8")
        try:
            read_matrix(p6)
        except ValueError as e:
            assert "Строка 2" in str(e), "Ошибка должна указывать на строку 2"
        else:
            assert False, "Ошибка не обнаружена: не число в ячейке"

        # 7. Лишние строки данных
        p7 = dir_path / "m7.txt"
        p7.write_text("1 1\n5\n6\n", encoding="utf-8")
        try:
            read_matrix(p7)
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена: лишние строки"

        # 8. Отсутствующий путь
        p8 = dir_path / "missing.txt"
        try:
            read_matrix(p8)
        except FileNotFoundError:
            pass
        else:
            assert False, "Ошибка не обнаружена: файл не найден"

def test_selected_sum():
    # Тест для 2 варианта (сумма отрицательных)
    m = [[1, -2, 3], [4, 0, -6]]
    assert selected_sum(m) == -8, "Ошибка в selected_sum для варианта 2"
    
    # Тест на отсутствие подходящих элементов
    m2 = [[1, 2], [3, 4]]
    assert selected_sum(m2) == 0

if __name__ == "__main__":
    test_read_matrix()
    test_selected_sum()
    print("Все тесты пройдены успешно!")
