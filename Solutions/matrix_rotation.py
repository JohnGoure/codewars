def rotate(matrix):
    """Rotate an N X N matrix 90 degrees to the left."""
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[y][x] = matrix[x][x]
    return matrix
