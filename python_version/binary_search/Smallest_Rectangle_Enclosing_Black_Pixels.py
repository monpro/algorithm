class Solution:
    def minArea(self, image, x, y):
        '''
        to find min area, you need to find left, right, up and down of 1 first shown position
        :param image: image mixed with 0 and 1, only 1 connected components of black pixels( all 1s')
        :param x: (x,y) position of one black pixel in image
        :param y:
        :return: the min area of rectangular which contains all black pixels
        '''
        row, column = x, y
        def row_empty(row_index):
            if row_index == -1 or row_index == len(image):
                return True
            for element in image[row_index]:
                if element == '1':
                    return False
            return True

        def col_empty(col_index):
            if col_index == -1 or col_index == len(image[0]):
                return True
            for row in image:
                for element in row[col_index]:
                    if element == '1':
                        return False
            return True
        def leftBoundary():
            left, right = -1, column
            while left + 1 < right:
                mid = left + (right - left) // 2
                if col_empty(mid) and not col_empty(mid + 1):
                    return mid
                elif col_empty(mid) and col_empty(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def rightBoundary():
            left, right = column, len(image[0])
            while left + 1 < right:
                mid = left + (right - left) // 2
                if col_empty(mid + 1) and not col_empty(mid):
                    return mid
                elif col_empty(mid) and col_empty(mid + 1):
                    right = mid
                else:
                    left = mid + 1
            return left


        def upBoundary():
            up,down = -1, row
            while up + 1 < down:
                mid = up + (down - up) // 2
                if row_empty(mid) and not row_empty(mid + 1):
                    return mid
                elif row_empty(mid) and row_empty(mid + 1):
                    up = mid + 1
                else:
                    down = mid
            return up

        def downBoundary():
            up,down = row, len(image)
            while up + 1 < down:
                mid = up + (down - up) // 2
                if not row_empty(mid) and row_empty(mid + 1):
                    return mid
                elif not row_empty(mid) and not row_empty(mid+ 1):
                    up = mid + 1
                else:
                    down = mid
            return up


        return ((rightBoundary() - leftBoundary())) * (downBoundary() - upBoundary())