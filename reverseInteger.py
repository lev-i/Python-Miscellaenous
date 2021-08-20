"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        # mod 10 pulls a digit, then we divide x by 10 to move onto the next digit
        if x >0:
            while x!=0:
                temp = int(x%10)
                x = int(x/10)
        # multiplying result by 10 pushes the other digits forward, and allows adding the next digit
                result = result * 10 + temp
        # negative numbers, room to optimize here
        if x < 0:
            x = abs(x)
            while x!=0:
                temp = int(x%10)
                x = int(x/10)
                result = result * 10 + temp
                if x ==0:
                    result = result*-1
        # int limits
        if result > 2**31-1:
            result = 0
        if result < -2**31:
            result = 0
        return result
