# LC - 75
# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        a = 0
        b = 0
        if len(nums) == 1: 
            return (nums[0] or k)
        for b in range(len(nums)):

            if nums[b] == 0 :
                k-=1
            
            if k < 0:
                if nums[a] == 0: 
                    k+=1 
                a+=1
        return b-a+1