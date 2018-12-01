class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        /*
         * clockwise rotate
         * first reverse up to down, then swap the symmetry
         * 1 2 3     7 8 9     7 4 1
         * 4 5 6  => 4 5 6  => 8 5 2
         * 7 8 9     1 2 3     9 6 3
        */
        """
        if len(matrix) == 0:
            return matrix
        if len(matrix[0]) == 0:
            return matrix

        left,right = 0, len(matrix) - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right],matrix[left]
            left+= 1
            right -= 1

        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]






