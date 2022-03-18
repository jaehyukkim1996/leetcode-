from typing import Optional

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"]": "[" ,")": "(", "}": "{"}  #key is closing parentheses

        for c in s:
            if c in closeToOpen:
                if stack is not None and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        print(stack)
        if stack is None:
            return True
        else:
            return False


solution = Solution()
result = solution.isValid("(({[]}))")
print(result)