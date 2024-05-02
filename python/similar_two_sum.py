# Leetcode: 2441. Largest Positive Integer That Exists With Its Negative
class Solution:

    def findMaxK(self, nums: List[int]) -> int:

        i = 0
        j = len(nums) - 1

        nums = sorted(nums)
        while (nums[i] < 0 and nums[j] > 0 and j > i):
            if abs(nums[i]) < nums[j]:
                j -= 1
            elif abs(nums[i]) > nums[j]:
                i += 1
            elif abs(nums[i]) == nums[j]:
                return nums[j]
        return -1
    