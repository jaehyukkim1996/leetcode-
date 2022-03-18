class Solution():
    def findNumber(self, list1, list2):
            hashMap = set(list1)
            print(hashMap)

            for i in range(len(list2)):
                if list2[i] in hashMap:
                    print("1")
                else:
                    print("0")



solution = Solution()
result = solution.findNumber([4,1,5,2,3], [1,3,7,9,5])

