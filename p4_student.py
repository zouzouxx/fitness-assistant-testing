def my_max(nums):
    if len(nums) == 0:
        return None
    champion = nums[0]
    for n in nums:
        if n > champion:
            champion = n
    return champion

print(my_max([]))
print(my_max([-5, -2, -8, -1]))
print(my_max([3, 8, 5, 7]))
print(my_max([5]))
