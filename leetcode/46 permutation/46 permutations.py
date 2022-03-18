class Solution:
    def permute(self, nums):
        prev = []
        answer = []
        def backtrack(elements):
            if len(elements) == 0:
                answer.append(prev[:])

            for e in elements:
                next = elements[:]
                prev.append(e)
                next.remove(e)
                backtrack(next)
                prev.pop()

        backtrack(nums)

        return answer




solution = Solution()
result = solution.permute([1,2,3])
print(result)