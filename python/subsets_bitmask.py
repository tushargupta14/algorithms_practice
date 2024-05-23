# Leetcode: https://leetcode.com/problems/subsets/?envType=daily-question&envId=2024-05-21
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        t = len(bin(2**len(nums)-1)[2:])
        # print(t)
        res = []
        for i in range(2**len(nums)):
            x = bin(i)[2:]
            n = t - len(x)
            x = ''.join('0' for j in range(n)) + x
            # print(x)
            res.append([k for i, k in zip(x, nums) if i == '1'])

        return (res)
