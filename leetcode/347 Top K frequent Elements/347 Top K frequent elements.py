class Solution(object):
    def topKFrequent(self, nums, k):

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] +=1
            else:
                hashMap[nums[i]] = 1

        order = sorted(list(hashMap.values()), reverse=True)

        orderK = order[k-1]

        result = []

        for key, value in hashMap.items():
            if value >= orderK:
                result.append(key)

        return result


solution = Solution()
result = solution.topKFrequent([1,1,1,2,2,3], 2)
print(result)