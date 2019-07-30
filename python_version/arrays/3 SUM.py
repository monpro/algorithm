class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        # combination of double pointer and hashmap
        numbers.sort()
        result = []
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                if numbers[left] + numbers[right] + numbers[i] > 0:
                    right -= 1

                elif numbers[left] + numbers[right] + numbers[i] < 0:
                    left += 1

                elif numbers[left] + numbers[right] + numbers[i] == 0:
                    if [numbers[i], numbers[left], numbers[right]] in result:
                        pass
                        left += 1
                        right -= 1
                    else:
                        result.append([numbers[i], numbers[left], numbers[right]])
                        left += 1
                        right -= 1

        return result

    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        result = None
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                amount = numbers[i] + numbers[left] + numbers[right]

                if result is None:
                    result = amount

                if abs(result - target) > abs(amount - target):
                    result = amount

                if amount < target:
                    left += 1

                elif amount > target:
                    right -= 1

                elif amount == target:
                    return amount

        return result

