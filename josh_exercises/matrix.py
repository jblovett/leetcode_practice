class Solution:
    def rotate(self, matrix):
        # n is the height and width of the matrix
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 -j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp
                

