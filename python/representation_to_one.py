# Leetcode: 1404. Number of Steps to Reduce a Number in Binary Representation to One
class Solution:
    def numSteps(self, s: str) -> int:
        
        steps = 0

        def add_1(s):
            carry = 1
            s = list(s)
            for j in range(len(s)-1, -1, -1):
                
                if (int(s[j]) + carry) == 1:
                    s[j] = '1'
                    carry = 0
                elif (int(s[j]) + carry) > 1 :
                    carry = 1
                    s[j] = '0' 
                
                # print(s, carry)
            if carry == 1:
                s = ['1'] + s
            
            return ''.join(i for i in s)

        while (len(s) > 1):

            # print(s)
            if s == '1':
                return steps

            if s[-1] == '1':
                # odd
                s = add_1(s)
                # print('Here')
            elif s[-1] == '0':
                s = s[:len(s)-1]
            
            steps += 1
 
        return steps
