# Leetcode: https://leetcode.com/problems/sum-of-all-subset-xor-totals/?envType=daily-question&envId=2024-05-20
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        seen = set()
        self.xor_sum = 0 

        def create_subsets(nums, i, xor_so_far, seen, idx_arr):
            # not required
            if i >= len(nums):
                self.xor_sum += xor_so_far
                seen.add(idx_arr)
                return
            
            if i == len(nums)-1:
                self.xor_sum += xor_so_far
                self.xor_sum += xor_so_far ^ nums[i]
                seen.add(idx_arr)
                seen.add(idx_arr + (nums[i], ))
                return
            
            create_subsets(nums, i+1, xor_so_far, seen, idx_arr)
            xor_so_far ^= nums[i] 
            create_subsets(nums, i+1, xor_so_far, seen, idx_arr + (nums[i],))

            return
 
        create_subsets(nums, 0, 0, seen, ())

        return self.xor_sum

