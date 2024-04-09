# leetcode: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/?envType=weekly-question&envId=2024-04-01
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        distinct_char = 0 
        i = 0 
        j = 0 

        maxl = 0
        l = 0
        seen = [0] * 26 

        hmap = defaultdict(int)

        while(j < len(s) and i < len(s)): 

            hmap[s[j]]+=1

            distinct_char = len(hmap)
            
            #print(i, j , s[i], s[j], seen, distinct_char)

            j+=1
            while (len(hmap) > 2): 
                
                hmap[s[i]]-=1
                if hmap[s[i]] == 0: 
                    del hmap[s[i]]
                i+=1

            maxl = max(maxl, j-i)
            #print('maxl', maxl)  

        return maxl







