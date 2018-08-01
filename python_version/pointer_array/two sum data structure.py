class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """
    array = []

    def add(self, number):
        # write your code here
        self.array.append(number)

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        hashmap = dict()

        for i in range(len(self.array)):
            if value - self.array[i] in hashmap:
                return True

            hashmap[self.array[i]] = i

        return False
