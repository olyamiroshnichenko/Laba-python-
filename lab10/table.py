def row_sums(matrix):
    
    if not matrix:
        return []
    return [sum(row) for row in matrix]

def column_sums(matrix):
   
    if not matrix:
        return []
    cols = len(matrix[0])
    return [sum(matrix[row][col] for row in range(len(matrix))) for col in range(cols)]
