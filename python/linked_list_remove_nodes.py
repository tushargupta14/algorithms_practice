# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Leetcode: https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        idx = 0
        # build a monotonic stack
        node = head
        while (node is not None):
            idx += 1
            while (len(stack) and node.val > stack[-1][0]):
                stack.pop()  
            stack.append((node.val, idx))
            node = node.next
        # print(stack)
        idx = 0
        node = head
        while (node is not None):
            idx += 1
            # print(idx, node.val)
            while (stack[0][1] < idx):
                stack.pop(0)
            if node.val < stack[0][0] and stack[0][1] > idx:
                # mark for deletion
                node.val = -1
            node = node.next
        
        while (head.val == -1):
            head = head.next
        node = head

        while (node.next is not None):
            temp = node.next
            while (temp.val == -1):
                temp = temp.next
            node.next = temp
            node = node.next

        return head