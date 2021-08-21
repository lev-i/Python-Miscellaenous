"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if list is empty
        if not strs:
            return ""
        # min is NOT the length, it is lexicographically
        shortest = min(strs)
        longest = max(strs)
        # enumerate gives you the count AND the value for each item
        for i, c in enumerate(shortest):
        # if the VALUE (c) in the shortest does not equal the VALUE in the longest at i
            if c != longest[i]:
                    return shortest[:i]
        return shortest
