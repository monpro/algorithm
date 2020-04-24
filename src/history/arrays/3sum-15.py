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
            if i > 0 and numbers[i - 1] == numbers[i]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                temp_value = numbers[left] + numbers[right] + numbers[i]
                if temp_value > 0:
                    right -= 1

                elif temp_value < 0:
                    left += 1

                elif temp_value == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])
                    while left < right and numbers[left] == numbers[left + 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1
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

