"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#       If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
#       If the sum is negative, it has no use to the next element, so we break.
        # start at 1 because we'll be looking at the previous digit
        for i in range(1, len(nums)):
            # if the previous integer is positive
            if nums[i-1] > 0:
            # add it to the current digit
                nums[i] += nums[i-1]
        return max(nums)
