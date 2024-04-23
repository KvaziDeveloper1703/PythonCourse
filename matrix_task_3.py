N = int(input())
M = int(input())

matrix=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    input_string = input()
    input_data = input_string.split()
    for j in range(M):
        matrix[i][j] = int(input_data[j])

maximum = 0
first_max_row = 0
first_max_column = 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            first_max_row = i
            first_max_column = j

print(first_max_row, first_max_column)