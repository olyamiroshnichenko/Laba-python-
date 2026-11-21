def transform(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            if element == 0:
                new_row.append(1)
            else:
                new_row.append(element)

        new_matrix.append(new_row)

    return new_matrix

def main():
    matrix = [[-2, 0, 3], [4, -5, 6]]

    print("Исходная матрица:")
    for row in matrix:
        print(*row)

    new_matrix = transform(matrix)

    print("Новая матрица:")
    for row in new_matrix:
        print(*row)

if __name__ == "__main__":
    main()
