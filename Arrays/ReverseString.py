def reverse(str):
    newStr = []
    for i in range(len(str)-1, -1, -1):
        newStr.append(str[i])

    return ''.join(newStr)

x = reverse("Hello")
print(x)

