#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 02-12-2021 14:02
# @Author  : Tushar Gupta
# Leetcode: https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        odd = tail = head
        even_head = even = head.next

        i = 1
        while (odd is not None or even is not None):
            # print(i)
            if (i % 2 == 0):
                # even
                if odd is not None:
                    even.next = odd.next
                    even = even.next
                else:

                    break

            elif (i % 2 != 0):
                # odd
                if (even is not None):
                    odd.next = even.next
                    odd = odd.next
                    if odd is not None:
                        tail = odd

                else:
                    # end of the list
                    tail = odd
                    break

            i += 1

        # print(even_head.val)
        tail.next = even_head

        return head











