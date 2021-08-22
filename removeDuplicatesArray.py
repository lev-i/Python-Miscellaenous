"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # sets...can't contain duplicates...sorting's actually redundant here since we're given a sorted array (technically a list since python doesn't use arrays)
        # so we convert the set back to a list
        nums[:] = sorted(set(nums))

#       alternatively, if can't use sets, x =1 as array is sorted so first item must be unique. we go through with i and x, i is the front runner, x is the slow runner. as long as no dupes are found, i prints to x. if a dupe is found, it's passed over.        
#       x = 1
#       for i in range(len(nums)-1):
# 	        if(nums[i]!=nums[i+1]):
# 		        nums[x] = nums[i+1]
# 		        x+=1
#       return(x)
