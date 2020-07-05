
def square_nums(nums):
    for num in nums:
        yield (num * num)


my_nums = square_nums([1, 2, 3, 4, 5])

print(my_nums)
print(next(my_nums))
print(next(my_nums))
for num in my_nums:
    print(num)
