#Write a program that rotates a matrix by 180 degrees.
#Input:
#1   2   3   4
#5   6   7   8
#9   10  11  12
#13  14  15  16
#Output:
#16  15  14  13
#12  11  10  9
#8   7   6   5
#4   3   2   1

def rotate_matrix_180(matrix):
    rotated_matrix = [line[::-1] for line in matrix[::-1]]
    return rotated_matrix

#Input
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

[print(line) for line in rotate_matrix_180(matrix)]
