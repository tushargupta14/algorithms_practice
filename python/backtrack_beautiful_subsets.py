# Leetcode: 2597. The Number of Beautiful Subsets
from collections import defaultdict
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        nmap = defaultdict(int)
        
        self.count = 0 

        def include(a, nmap, k): 
            if nmap[a - k] > 0:
                return False
            return True
        
        def subsets(i, nums, nmap):
            if i >= len(nums):
                # print(res)
                self.count += 1
                return

            # Pick the number
            if include(nums[i], nmap, k):
                nmap[nums[i]] += 1
                subsets(i+1, nums, nmap)  
                nmap[nums[i]] -= 1
            subsets(i+1, nums, nmap)

            return

        subsets(0, nums, nmap)
        return self.count - 1