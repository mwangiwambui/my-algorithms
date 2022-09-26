# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        # basecase
        if length == 1:
            return False
        
        nums.sort()
        i = 0;
        while i < length - 1:
            if nums[i] == nums[i+1]:
                return True        
            i = i+1
        return False     
                