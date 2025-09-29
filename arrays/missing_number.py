class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        total_sum = 0
        for i in range(n + 1):
            total_sum += i
        
        for i in range(n):
            total_sum -= nums[i]
        
        return total_sum
            