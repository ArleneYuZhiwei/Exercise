# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:52:21 2018

@author: 11
"""

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """   
    if len(nums)==0:
        return 0
    total=nums

    if len(nums)>=3:
        total[2]=total[0]+total[2]
        for i in range(3,len(nums)):  
                total[i]+=max(total[i-2],total[i-3])  
            
    print (total)
    return (max(total))

rob([1,7,9,2])