def sum_evens(nums):
    a = 0
    for n in nums:
        if n % 2 == 0:
            a = a + n
    return a

def filter_above(nums, limit):
    result = []
    for n in nums:
        if n > limit:
            result.append(n)
    return result

def count_a(s):
    count = 0
    for ch in s:
        if ch == 'a':
            count = count + 1
    return count

def my_max(nums):
    result = nums[0]
    for n in nums:
        if n > result:
            result = n
    return result

print("P1 空列表:", sum_evens([]))
print("P1 全奇数:", sum_evens([1, 3, 5]))
print("P2 空列表:", filter_above([], 60))
print("P2 等于limit:", filter_above([60, 61], 60))
print("P3 空字符串:", repr(count_a("")))
print("P3 大写A:", count_a("Apple"))
print("P4 单元素:", my_max([5]))
print("P4 空列表:", my_max([]))
