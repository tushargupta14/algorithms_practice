#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 28-11-2021 16:56
# @Author  : Tushar Gupta
# Leetcode : https://leetcode.com/problems/interval-list-intersections/


class Solution(object):

    def merge(self, firstList, secondList):

        merged = []

        i = 0
        j = 0

        while (i < len(firstList) or j < len(secondList)):

            if (firstList[i][0] <= secondList[j][0]):
                merged.append(firstList[i])
                i += 1
            else:
                merged.append(secondList[j])
                j += 1

            if (i == len(firstList)):
                while (j < len(secondList)):
                    merged.append(secondList[j])
                    j += 1
                break
            if (j == len(secondList)):
                while (i < len(firstList)):
                    merged.append(firstList[i])
                    i += 1
                break

        return merged

    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        if (len(firstList) == 0 or len(secondList) == 0):
            return []
        merged = self.merge(firstList, secondList)

        start = merged.pop(0)
        s = start[0]
        e = start[1]

        res = []
        while (len(merged) > 0):

            curr = merged.pop(0)
            curr_s = curr[0]
            curr_e = curr[1]

            if (curr_s > e):
                s = curr_s
                e = curr_e
                continue

            res.append([max(s, curr_s), min(e, curr_e)])

            s = min(e, curr_e)
            e = max(e, curr_e)

        return res

if __name__ == '__main__':
    s = Solution()

