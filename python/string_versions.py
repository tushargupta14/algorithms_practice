# Leetcode: https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2024-05-03
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        one = version1.split('.')
        two = version2.split('.')

        i, j = 0, 0
        while (i < len(one) or j < len(two)):

            a = int(one[i]) if i < len(one) else 0
            b = int(two[j]) if j < len(two) else 0

            if a < b:
                return -1
            elif a > b: 
                return 1
            elif a == b:
                i += 1
                j += 1
        return 0