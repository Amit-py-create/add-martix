def add_matrices(matrix1, matrix2):
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")

    # Create a result matrix initialized with zeros
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    # Add corresponding elements of the matrices
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# Example usage
if __name__ == "__main__":
    # Define two matrices
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Add the matrices
    result_matrix = add_matrices(matrix1, matrix2)

    # Print the result
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)
