class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in hashMap:
                return [nums[hashMap[diff]], nums[index]]
            else:
                hashMap[value] = index






ob1 = Solution()
print(ob1.twoSum([1,2,3,4,5,6,7,8,9], 9))