import random

matrix=[[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        matrix[i][j] = random.randint(10,99)

maximum = 10
max_row = 0
max_column = 0

minimum = 99
min_row = 0
min_column = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]
            max_row = i
            max_column = j
        if matrix[i][j] < minimum:
            minimum = matrix[i][j]
            min_row = i
            min_column = j

print("Матрица А: ")

for line in matrix:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)

print("Максимальный элемент А[" + str(max_row) + "," + str(max_column) + "]=" + str(maximum))
print("Минимальный элемент А[" + str(min_row) + "," + str(min_column) + "]=" + str(minimum))