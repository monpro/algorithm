class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        result = []

        if len(matrix) == 1:
            for i in matrix[0]:
                result.append(i)
            return result
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                result.append(matrix[i][0])
            return result

        while matrix:
            for i in matrix[0]:
                result.append(i)

            matrix = matrix[1:]
            print("matrix",matrix)
            if len(matrix) > 1:
                new_matrix = [[] for _ in range(len(matrix[0]))]
            else:
                new_matrix = []
            #then reverse matrix
            if len(new_matrix) > 1:
                for i in range(len(new_matrix) - 1, -1, -1):
                    for j in range(len(matrix)):
                        print(i)
                        new_matrix[len(new_matrix) - 1 - i].append(matrix[j][i])

                matrix = new_matrix
            else:
                for i in range(len(matrix[0]) - 1, -1, -1):
                    result.append(matrix[0][i])

                return result





l = Solution()
print(l.spiralOrder([
[6],[7],[9]
]))

