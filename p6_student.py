def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("abc"))
print(reverse_string(""))
print(reverse_string("a"))
