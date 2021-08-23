"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if list is empty
        if len(digits) == 0:
            digits = [1]
        # if last digit is a 9
        elif digits[-1] == 9:
            # take off the last digit, and add one to the "new" last digit
            digits = self.plusOne(digits[:-1])
            # add a zero to the end
            digits.extend([0])
        else:
            digits[-1] += 1
        
        return digits
