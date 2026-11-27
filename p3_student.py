def count_a(s):
    count = 0
    for ch in s:
        if ch.lower() == 'a':
            count = count + 1
    return count

print(count_a("banana"))
print(count_a("Apple"))
print(count_a(""))
