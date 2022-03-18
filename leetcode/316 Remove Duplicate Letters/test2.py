from typing import Optional

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        for i, ch in enumerate(s):
            if ch not in seen:
                while stack and ch < stack[-1] and last[stack[-1]] > i:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(ch)
                seen.add(ch)
        return ''.join(stack)

solution = Solution()
result = solution.removeDuplicateLetters("cbacdcbc")
print(result)

