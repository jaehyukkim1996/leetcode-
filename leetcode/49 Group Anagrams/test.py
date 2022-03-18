import operator

class Solution():
    def groupAnagrams(self, strings):
        hashMap = {}
        # put into hashMap (sorted : [arr])
        for i in range(len(strings)):
            x = "".join(sorted(strings[i]))
            if x not in hashMap:
                hashMap[x] = 1
            else:
                hashMap[x] += 1

        print(hashMap)

        print(sorted(hashMap, key=lambda key: len(hashMap[key])))




solution = Solution()
result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])

