class QuickSort:
    def sortInteger(self,array):
        self.quicksort(array, 0, len(array) - 1)
        print(array)

    def quicksort(self,array,start,end):
        if start >= end:
            return
        left,right = start, end
        # key points 1: pivot is the value, not the index
        pivot = array[start]
        # key point 2: every time you compare left & right
        # it should be left <= right
        while left <= right:
            while left <= right and array[left] < pivot:
                left += 1
            while left <= right and array[right] > pivot:
                # key points 3: A[right] > pivot
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        self.quicksort(array, start, right)
        self.quicksort(array, left, end)


if __name__ == "__main__":
    import random
    l = QuickSort()
    array = []
    for i in range(100):
        array.append(int(random.random() * 1000))
    print(array)
    l.sortInteger(array)
