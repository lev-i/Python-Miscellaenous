"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # array (stack)
        stack = []
        # dict key:value
        dict = {"]":"[", "}":"{", ")":"("}
        # going through the string
        for i in s:
            # if an opener is found, add it to the stack
            if i in dict.values():
                stack.append(i)
            # if a closer is found and the stack is empty or its opener cannot be popped off the stack, return False
            elif i in dict.keys():
                if stack ==[] or dict[i]!=stack.pop():
                    return False
            # cover all other cases
            else:
                return False
        # is the stack empty? if it is, all parentheticals were closed
        return stack == []
