"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # r = x
        # while r*r > x:
        #     r = (r + x/r) / 2
        # return int(r)
    
        lo, hi = 0, x
        while lo <= hi:
            # calculate mid point between high and low
            mid = lo + (hi-lo) // 2
            # if x is between mid^2 and (mid+1)^2, then mid is the square root
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            # if mid^2 is larger than x, we need to reduce mid
            elif x < mid*mid:
                hi = mid - 1
            # if mid^2 is smaller than x, we need to increase mid
            else:
                lo = mid + 1
