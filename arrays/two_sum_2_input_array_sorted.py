class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0 
        right = len(numbers) - 1
        result = []

        while (left < right):
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                result = [left + 1, right + 1]
                break
            elif target > current_sum:
                left += 1
            else:
                right -= 1
        return result