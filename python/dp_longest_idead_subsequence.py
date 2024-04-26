

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        """LC 370. Longest Ideal Subsequence

        Returns:
            int: length of the longest ideal 
            subsequence within s where 
            ord|t[i+1] - t[i]| < k
        """
        seen = {s[0] : 0}
        dp = [1] * len(s)
        for i in range(1, len(s)):    
            max_len = 0
            for j in range(-k, k+1, 1):
                char = chr(ord(s[i]) + j)
                if char in seen and seen[char] < i:
                    if dp[seen[char]] + 1 > max_len:
                        dp[i] = dp[seen[char]] + 1
                        max_len = dp[i]
            seen[s[i]] = i

        return max(dp)