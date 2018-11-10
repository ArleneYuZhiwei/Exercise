# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:31:31 2018

@author: 11
"""
def  maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """   
    if len(nums)==0:
        return 0
    total=nums[0]
    tmp=0
    for i in range(0,len(nums)):  
        if tmp+nums[i]<nums[i]:
            tmp=nums[i]
        else:
            tmp+=nums[i]
        if total<tmp:
            total=tmp 
        print ("i",i)
        print ("total",total)
        print ("tmp",tmp)
        
    print (total)
    return (total)
                
maxSubArray([-3,2,5,6])
