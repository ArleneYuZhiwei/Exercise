class Solution(object):   
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        for i,s in enumerate(nums):
            if s==0:
                find = False
                for j in range(1, i+1):
                    if nums[i-j]>j or i==len(nums)-1 and nums[i-j]==j:
                        find=True
                        break
                if not find:
                    return False
            
            
        return True

 

        