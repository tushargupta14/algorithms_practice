#https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        count = 0 

        a = 0 
        b = len(nums) - 1
        print(nums)
        while( b > a ):

            if nums[b] + nums[a] < k: 

                a+=1
            elif nums[b] + nums[a] > k: 
                b-=1
            else : 
                count+=1
                b-=1
                a+=1
            
        

        return count