class Solution(object):
    def letterCombinations(self, digits):
        result = []

        if digits == "":
            return result

        dic = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        stack = [("", 0)]
        while stack:
            word, index = stack.pop()

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    stack.append((word +j, i+1))

            if len(word) == len(digits):
                result.append(word)

        return result

solution = Solution()
result = solution.letterCombinations("23")
print(result)
