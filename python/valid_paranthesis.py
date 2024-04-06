# Leetcode: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/?envType=daily-question&envId=2024-04-06

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []

        for i, char in enumerate(s): 
            if char in '()':
                if len(stack) > 0 and stack[-1][0] == '(' and char == ')': 
                    #print(char, i)
                    stack.pop()
                else : 
                    stack.append((char, i))
        while (len(stack) > 0): 

            _, i = stack.pop()
            s = s[:i] + s[i+1:]

        return s