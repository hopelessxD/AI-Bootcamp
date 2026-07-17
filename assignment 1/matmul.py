def get_matrix(name, rows=2, cols=2):
    print(f"Enter {rows}x{cols} Matrix {name}:")
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = [int(x) for x in input(f"Row {i + 1}: ").split()]
                if len(row) != cols:
                    raise Exception
                matrix.append(row)
                break
            except Exception:
                print("Invalid input")
    return matrix

A = get_matrix("A")
B = get_matrix("B")

C = [
    [sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
    for i in range(2)
]

print("Result Matrix:")
for row in C:
    print(f"[ {' '.join(f'{val:1d}' for val in row)} ]")