class Solution:
    def arrPush(self, arr, element, targetIndex):
        result = []

        for index, value in enumerate(arr):
            if index == targetIndex:
                result.append(element)
                result.append(value)
            else:
                result.append(value)


        return result


solution = Solution()
answer = solution.arrPush([1,2,3,4,5,6], 10, 4)

print(answer)


