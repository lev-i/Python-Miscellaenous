"""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # a number ^= to itself is 0
        # Commutative law means array does not need to be sorted to arrive at the correct answer
        for i in nums:
            res ^= i
        return res
