strs = "{{[[(())]]}}"
opener = "{[("
pair = {")":"(", "}":"{", "]": "["}
stack = []

for letters in strs:
    if letters not in opener:
        if not stack:
            print("False")
        top = stack.pop()
        if pair[letters] != top:
            print("False")
    else:
        stack.append(letters)

if not stack:
    print("True")