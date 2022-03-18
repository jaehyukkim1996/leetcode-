class Solution(object):
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)

        ans = [0] * length

        for i in range(length):
            for j in range(i+1, length):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break

        return ans


solution = Solution()
result = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(result)