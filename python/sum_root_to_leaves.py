# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self): 
        self.nums = 0 

    

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        path = ''
        def dfs(node, nums, path): 

            if node is None: 
                return
            
            path+= str(node.val)

            # Leaf node
            if not node.left and not node.right:  
                #print(path)
                self.nums+=int(path)
                return
            
            # Not a leaf node
            dfs(node.right, nums, path)
            dfs(node.left, nums, path)

            return 

        dfs(root, self.nums, path)

        return self.nums
