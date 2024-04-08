
# Leetcode: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:



        while(len(students) > 0):

            if students[0] ==  sandwiches[0]: 
                students = students[1:]
                sandwiches = sandwiches[1:]

            elif students[0] != sandwiches[0]: 
                temp = students[0]
                students = students[1:]
                students.append(temp)
            
            flag = 0 
            for i in range(len(students)): 

                if students[i] == sandwiches[0]: 
                    flag = 1
                    break
            
            if flag == 0: 
                return len(students)


        return 0
