'''
1 2 3 4                     1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
5 6 7 8             ----->>>
9 10 11 12
13 14 15 16


'''

# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         length = 0
#         for i in matrix:
#             for j in i:
#                 length += 1
#         result = []
#
#
#         count = 0
#         column_flag = True
#
#         row_start, column_start  = 0, 0
#         row_end, column_end = len(matrix),len(matrix[0])
#         while count < length:
#             if column_flag:
#                 if row_start < row_end:
#                     pass
#                 else:
#                     row_start -= 1
#                     row_end -= 1
#
#                     if column_start < column_end:
#                         pass
#                     else:
#                         column_start -= 1
#                         column_end -= 1
#                 for i in range(column_start,column_end):
#                     result.append(matrix[row_start][i])
#                     print(i)
#                     print(result)
#
#
#                 row_start += 1
#                 column_start, column_end = column_end, column_start
#                 column_flag = False
#             else:
#                 if row_start < row_end:
#                     pass
#                 else:
#                     row_start -= 1
#                     row_end -= 1
#                 if column_start < column_end:
#                     pass
#                 else:
#                     column_start -= 1
#                     column_end -= 1
#                 for i in range(row_start,row_end):
#                     print(column_start)
#
#                     result.append(matrix[i][column_start])
#                 column_start -= 1
#                 row_start, row_end = row_end, row_start
#                 column_flag = True
#
#         return  result


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        result = []
        while(matrix):
            result += matrix.pop(0)
            if len(matrix) == 0:
                break
            matrix = self.turn(matrix)

        return result

    def turn(self,matrix):
        row = len(matrix)
        column = len(matrix[0])

        new_matrix = []
        for i in range(column - 1, -1, -1):
            temp = []
            for j in range(row):
                temp.append(matrix[j][i])
            new_matrix.append(temp)


        return new_matrix



l = Solution()
m  = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(l.printMatrix(m))



