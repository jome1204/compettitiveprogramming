class Solution(object):
    def spiralOrder(self, matrix):
        if matrix == None or matrix == []:
            return matrix
        else:
            #no of rows
            a = len(matrix)
            #no of columns
            c = len(matrix[0])

            k = 0

            l = 0
            spiral = []

            while k < a and l < c:

                for i in range(l, c):
                    spiral.append(matrix[k][i])
                k += 1


                for i in range(k, a):
                    spiral.append(matrix[i][c-1])
                c-= 1


                if k < a:
                    for i in range(c-1, l-1, -1):
                        spiral.append(matrix[a-1][i])

                    a -= 1

                #print the first column from the remaining columns
                if l < c:
                    for i in range(a-1, k-1, -1):
                        spiral.append(matrix[i][l])

                    l += 1

            return spiral
