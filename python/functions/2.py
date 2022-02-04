def reversestring(s):
    str = ""
    for i in s:
        str = i + str
    return str

alpha = input("enter a string: ")
print(reversestring(alpha))