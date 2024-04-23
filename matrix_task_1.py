N = int(input())
M = int(input())

mult=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        mult[i][j] = i * j

for line in mult:
    output_string = ""
    for character in line:
        output_string += str(character) + " "
    print(output_string)