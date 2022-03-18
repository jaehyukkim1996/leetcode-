class Solution():
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        l = []
        for i in range(len(s)):
            ans = ""
            for j in range(i, len(s)):
                ans += s[j]
                print(ans)
                if ans == ans[::-1]:
                    l.append(ans)

        print(l)
        return max(l, key=len)




solution = Solution()
result = solution.longestPalindrome("abbaaaaa")
print(result)
