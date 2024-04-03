
# Leetcode: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
class Solution:


    def __init__(self): 
        self.good_nodes = 0

    def DFS(self, root, max_on_path):

        if root is None: 
            return
        
        if root.val >= max_on_path: 
            self.good_nodes = self.good_nodes + 1
        else : 
            max_on_path = root.val
        
        self.DFS(root.right, max_on_path)
        self.DFS(root.left, max_on_path)
        
        return


    def goodNodes(self, root: TreeNode) -> int:

        max_on_path = root.val

        self.DFS(root, max_on_path)

        return self.good_nodes