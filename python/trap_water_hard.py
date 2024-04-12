# Leetcode: https://leetcode.com/problems/trapping-rain-water/?envType=daily-question&envId=2024-04-12
class Solution:
    def trap(self, height: List[int]) -> int:


        left = []
        right = [-1]*len(height)
        max_el = - 1000
        for i in range(len(height)): 
            max_el = max(max_el, height[i])
            left.append(max_el)

        max_el = - 1000
        for i in range(len(height)-1, -1, -1): 
            #print(i)
            max_el = max(max_el, height[i])
            right[i] = max_el
        # print(left)
        # print(right)
        water = 0 
        for i in range(len(height)): 

            water+= min(left[i], right[i]) - height[i]

        return water