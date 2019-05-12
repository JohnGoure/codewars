def rotate(matrix):
    """Rotate an N X N matrix 90 degrees to the left."""
    for x in range(len(matrix) - 1, 0, -1):
        for y in range(len(matrix)):
            matrix[x][y] = matrix[x][x]
    return matrix
