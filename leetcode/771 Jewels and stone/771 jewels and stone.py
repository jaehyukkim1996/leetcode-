class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # Create a hash set
        hashSet = set(jewels)
        count = 0

        for i in range(len(stones)):
            if stones[i] in hashSet:
                count += 1

        return count


solution = Solution()
result = solution.numJewelsInStones("Aa", "aAAbbbb")
print(result)