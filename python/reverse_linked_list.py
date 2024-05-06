# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Leetcode: 206. Reverse Linked List
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head
        curr = head

        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev