# Write a function called find_min() that finds the smallest number in an array
def find_min(nums):
    min = float("inf")
    for num in nums:
        if num < min:
            min = num
    return min


def test(nums):
    min = find_min(nums)
    print(f"min is {min}")


test([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7])
test([4, 3, 2, 1, 18, 1, 2, 3, 4, 5, 6, 7])
test([43, 234, 65465, 234, 2343, 443, 2123, 8768])
test([])
test(
    [
        54,
        545,
        453,
        2,
        65,
        4,
        7,
    ]
)
