# Day 1

def get_data():
    with open("day_1_data.txt") as f:
        nums = [int(line) for line in f]

    return nums

def part1(nums):
    increased = 0
    prev = nums[0]  # Previous is initialised to the first number
    nums = nums[1:]  # Start from the second number
    for i in nums:
        if i > prev:
            increased += 1
        prev = i

    print("Part1 increased:", increased)


def get_window_slice_3_nums(nums, size):
    """ Returns window slices of a list of nums """
    return [nums[i:i+size] for i in range(len(nums)-(size-1))]


def part2(nums):
    increased = 0
    # Previous is initialised to the first window slice sum
    prev = sum(nums[0:3])
    # Start from the second number with window size of 3
    windows = get_window_slice_3_nums(nums[1:], size=3)

    for slice in windows:
        slice_sum = sum(slice)

        if slice_sum > prev:
            increased += 1
        prev = slice_sum

    print("Part2 increased:", increased)


nums = get_data()
part1(nums)
part2(nums)
