def sum_evens(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total = total + n
    return total
print(sum_evens([1, 2, 3, 4]))
