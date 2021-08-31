"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sets can't contain duplicates, so if the list is longer there must be at least one duplicate
        # return len(set(nums)) != len(nums)
        
        # sorting the list then iterating through it
        count = 1
        n = 2
        nums.sort()
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                count+=1
            elif nums[i] != nums[i-1]:
                if count >=n:
                    return True
                    count = 1
        if count >=n:
            return True
        return False
