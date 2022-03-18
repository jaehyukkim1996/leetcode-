class Solution(object):
    def groupAnagrams(self, strings):
        anagrams = dict()
        anagramGroups = []

        for string in strings:
            sortedString = "".join(sorted(string))
            stringList = anagrams.get(sortedString)

            if stringList is None:
                anagrams[sortedString] = []
            anagrams[sortedString].append(string)

        print(anagrams)

        for sortedString in anagrams:
            anagramGroups.append(anagrams[sortedString])

        return anagramGroups

result = Solution()
final = result.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(final)

