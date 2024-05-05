#Leetcode: 881. Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        if len(people) == 1: 
            return 1
        i, j = 0, len(people) - 1
        ans = 0 
        people = sorted(people)
        while (j > i):

            if people[i] + people[j] == limit:
                ans += 1
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                j -= 1
                ans += 1
            elif people[i] + people[j] < limit:
                i += 1
                j -= 1
                ans += 1
        if (j == i):
            ans += 1
        return ans
