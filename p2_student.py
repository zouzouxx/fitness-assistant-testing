def filter_above(nums, limit):
    filtered = []
    for n in nums:
        if n > limit:
            filtered.append(n)
    return filtered

print(filter_above([45, 80, 66, 59, 91], 60))
