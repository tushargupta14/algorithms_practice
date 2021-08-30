#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 29-08-2021 22:07
# @Author  : Tushar Gupta
# Leetcode problem: BST check sum IV

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def traverse_tree(self, root, node_set, k):

        if root is None:
            return False
        is_found_left = self.traverse_tree(root.left, node_set, k)
        if k - root.val in node_set:
            return True
        else:
            node_set.add(root.val)
        is_found_right = self.traverse_tree(root.right, node_set, k)

        return is_found_left | is_found_right

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        node_set = set()
        if (root.left is None and root.right is None):
            return False
        ## Tree traversal
        return self.traverse_tree(root, node_set, k)

if __name__ == '__main__':
    s = Solution()