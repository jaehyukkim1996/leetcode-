s = "bcabcbd"
sArr = []
for x in s:
    sArr.append(x)
length = len(sArr)

hashMap = {}

for i in range(length):
    if sArr[i] in hashMap:
        hashMap[sArr[i]] +=1
    else:
        hashMap[sArr[i]] = 1

res = []

for key in hashMap:
    val = hashMap[key]
    if val == 1:
        res.append(key)
    else:
        res.append(key)

sortedRes = sorted(res)
answer = "".join(sortedRes)
print(answer)






