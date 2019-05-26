class QuickSort:
    def sortInteger(self,array):
        self.quicksort(array, 0, len(array) - 1)
    def quicksort(self, array, start, end):
        if start >= end:
            return
        left, right = start, end
        # pviot is a value
        pviot = array[start]

        while left < right:
            while left < right and array[left] <= pviot:
                left += 1
            while left < right and array[right] >= pviot:
                right -= 1

            if left < right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        self.quicksort(array,start,right)
        self.quicksort(array,left, end)


