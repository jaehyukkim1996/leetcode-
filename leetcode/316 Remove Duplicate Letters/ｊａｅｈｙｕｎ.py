from collections import defaultdict

# using Stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # O(N)

        # char_count = Counter(s)
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1

        char_in = set()
        char_stack = list()
        char_list = list(s)
        # O(N) + O(N)
        for c in char_list:
            char_count[c] -= 1

            if c in char_in:
                continue２

            while char_stack:
                if char_stack[-1] < c:
                    break
                elif char_count[char_stack[-1]] == 0:
                    break
                else:
                    out = char_stack.pop()
                    char_in.remove(out)

            char_in.add(c)
            char_stack.append(c)

        return "".join(char_stack)

solution = Solution()
print(solution.removeDuplicateLetters("bcabc"))