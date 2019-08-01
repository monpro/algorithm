class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """

    def swap(self, A, a, b):
        temp = A[b]
        A[b] = A[a]
        A[a] = temp

    def rerange(self, A):
        if len(A) <= 1:
            return A
        positive = len([i for i in A if i > 0])
        negative = len([i for i in A if i < 0])
        positiveFirst = True
        if positive > negative:
            pass
        else:
            positiveFirst = False

        slow, fast = 0, 0
        while slow < len(A):
            if fast == len(A):
                fast = slow
            if positiveFirst:
                if A[fast] > 0:
                    # A[fast], A[slow] = A[slow], A[fast]
                    self.swap(A, fast, slow)
                    slow += 1
                    positiveFirst = not positiveFirst
            else:
                if A[fast] < 0:
                    # A[fast], A[slow] = A[slow], A[fast]
                    self.swap(A, fast, slow)
                    slow += 1
                    positiveFirst = not positiveFirst

            fast += 1

