"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Constraints:
1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        distinct_ways = 0
        two_steps = 1
        one_step = 2
        for i in range(2,n,1):
            distinct_ways = two_steps + one_step
            two_steps = one_step
            one_step = distinct_ways
        return distinct_ways
