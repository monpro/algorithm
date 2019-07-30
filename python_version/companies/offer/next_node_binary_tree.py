import math

class QuickSort():
    def __init__(self, array = []):
        self.array = array
        self.quick_sort_two_function(0,len(self.array) - 1)

        print(self.array)

    def quick_sort_one_function(self,left,right):
        if left >= right:
            return
        low = left
        high = right
        key = self.array[low]
        while left < right:
            while left < right and self.array[right] > key:
                right -= 1
            self.array[left] = self.array[right]
            while left < right and self.array[left] <= key:
                left += 1
            self.array[right] = self.array[left]
        self.array[right] = key
        self.quick_sort_one_function(low, left - 1)
        self.quick_sort_one_function(left + 1, high)

    def quick_sort_two_function(self,left,right):
        if left >= right:
            return
        low = left
        high = right
        pivoit = self.array[low]
        while left < right:
            while left < right and self.array[right] > pivoit:
                right -= 1
            while left < right and self.array[left] <= pivoit:
                left += 1
            self.array[left], self.array[right] = self.array[right], self.array[left]

        self.array[left], self.array[low] = self.array[low],self.array[left]

        self.quick_sort_two_function(low,left - 1)
        self.quick_sort_two_function(left + 1, high)









L = QuickSort([1,3,-2,8,9,1,4,5])
