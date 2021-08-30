#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 30-08-2021 13:00
# @Author  : Tushar Gupta


class Solution(object):

    def find_position(self, int_num, num_array, k):
        # print(num_array)
        if len(num_array) == 0:
            return 0
        i = 0
        while (i<k):
            #print(i)
            print(num_array)
            if i < len(num_array) and int_num >= num_array[i]:
                return i
            elif i == len(num_array):
                return k
            i+=1
            # for i in range(len(num_array)):
        #     if int_num >= num_array[i]:
        #         return i
        #     elif int_num < num_array[i]:
        #         continue
        return i

    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        num_array = []

        for num in nums:
            int_num = int(num)
            # find position
            index = self.find_position(int_num, num_array, k)
            print(index, num)
            if index < len(num_array):
                num_array.insert(index, int_num)
            elif index == 0 or index ==k:
                num_array.append(int_num)
        print(num_array)
        return str(num_array[k - 1])


if __name__ == '__main__':
    s = Solution()
    print(s.kthLargestNumber(["1","0","0"], 2))
