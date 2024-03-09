def read_matrix():
    matrix = []
    print("Please input your matrix below: ")
    while True:
        row_input = input().strip()
        if not row_input:
            break
        row = list(map(int, row_input.split()))
        matrix.append(row)
    return matrix

def scalar_multiplication(matrix, scalar):
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

def transpose(matrix):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed

if __name__ == "__main__":
    # Read the matrix
    original_matrix = read_matrix()
    print("Your matrix:")
    print('[[{}]'.format(', '.join(map(str, original_matrix[0]))), end='')
    for row in original_matrix[1:]:
       print(', [{}]'.format(', '.join(map(str, row))), end='')
    print(']')
    # Scalar multiplication
    scalar = 8
    scalar_multiplied_matrix = scalar_multiplication(original_matrix, scalar)
    print("\nScalar multiplication with {}:".format(scalar))
    print('[[{}]'.format(', '.join(map(str, row))), end='')
    for row in scalar_multiplied_matrix[0:]:
        print(', [{}]'.format(', '.join(map(str, row))), end='')
    print(']')
    # Transpose
    transposed_matrix = transpose(original_matrix)
    print("\nTransposition:")
    print('[[{}]'.format(', '.join(map(str, transposed_matrix[0]))), end ='')
    for row in transposed_matrix[1:]:
     print(', [{}]'.format(', '.join(map(str, row))), end='')
    print(']')
    