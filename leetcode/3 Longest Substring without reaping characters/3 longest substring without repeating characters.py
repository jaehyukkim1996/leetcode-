class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = ""
        subNoRepeat = ""
        hashMap = {}
        count = 1
        countArr = []

        for i in range(len(s)):
            sub = s[i]
            for j in range(i+1, len(s)):
                sub += s[j]
                # print(sub)

                if s[j] in hashMap:
                    hashMap = set(sub)
                    # print("yes")
                    # print(hashMap)
                    count = 1
                else:
                    hashMap = set(sub)
                    # print(hashMap)
                    count += 1
                    countArr.append(count)

        return max(countArr)





solution = Solution()
result = solution.lengthOfLongestSubstring("bbbbb")
print(result)