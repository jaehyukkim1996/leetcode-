test_dict = {'is': [1, 2], 'gfg': [3], 'best': [1, 3, 4]}

dict_dummy = {}
for key in test_dict:
    dict_dummy[key] = len(test_dict[key])

# arr for len of each key value list
arr = []

for key in dict_dummy:
    arr.append(dict_dummy[key])

sortedArr = sorted(arr, reverse=False)


def get_key(val, dict):
    for key, value in dict.items():
        if val == value:
            return key


final_dict = {}

for i in range(len(sortedArr)):
    key = get_key(sortedArr[i], dict_dummy)
    final_dict[key] = test_dict[key]

print(final_dict)
