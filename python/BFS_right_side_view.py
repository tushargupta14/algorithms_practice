# Leetcode: https://leetcode.com/problems/binary-tree-right-side-view/description/
import queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        ans = []
        
        if root is not None:
            stack.append(root)

        while(len(stack)): 
            #intermediate = []
            ans.append(stack[-1].val)
            
            i = len(stack)
            for _ in range(i): 

                el = stack.pop(0)

                if el.left : 
                    stack.append(el.left)

                if el.right : 
                    stack.append(el.right)

            #stack = intermediate
                

        return ans
            

