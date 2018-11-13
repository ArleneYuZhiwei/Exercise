# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:59:21 2018

@author: 11
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num2id = {}
        for i in range(len(nums)):
            num2id[nums[i]] = i
            
        for i in range(len(nums)):
            left = target - nums[i]
            if left in  num2id and  num2id[left] > i:
                return [i,num2id[left]]
