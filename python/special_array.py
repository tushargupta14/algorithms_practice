# Leetcode: https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        i = 0
        j = 0 
        nums = sorted(nums)
        n = len(nums)

        while (i < n):
            if nums[i] < j:
                while (i < n and nums[i] < j):
                    i += 1
                continue
            elif nums[i] == j:
                if j == n-i:
                    return j
                j += 1
                i += 1
            elif nums[i] > j:
                if j == n-i:
                    return j
                j += 1

        return -1
