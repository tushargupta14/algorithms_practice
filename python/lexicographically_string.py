# Leetcode: https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
    
        res = ''
        for i, c in enumerate(s):
            if c =='a': 
                res+='a'
                continue
            #print(c)
            flag = 0 
            for i in range(0, 26): 
                # transform the ordinals in the space of 0 to 25
                dist = min(ord(c) - ord('a') - i, ord('a') + i + 26 - ord(c))
                
                if dist <=k: 
                    #print(chr(ord('a')+i), dist)
                    res+= chr(ord('a') + i)
                    k-=dist
                    flag = 1
                    break

            if flag == 0:
                res+=c 


        return res
