# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Leetcode: 2816. Double a Number Represented as a Linked List
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            prev, curr = None, head

            while (curr):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        r_head = reverse(head)
        curr = r_head
        carry = 0
        # print(curr)
        while (curr):
            prod = curr.val * 2 + carry
            carry = prod // 10
            curr.val = prod % 10
            if carry != 0 and curr.next is None:
                newNode = ListNode(carry)
                curr.next = newNode
                curr = newNode
                break
            curr = curr.next
        return reverse(r_head)
