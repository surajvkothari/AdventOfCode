# Advent of code 2020
# Day 9

""" Part 1 """
def get_data():
    with open("day9_data.txt") as f:
        data = [int(i.strip()) for i in f]

    return data


def check_sum(nums, target):
    for i in nums:
        for j in nums:
            if i != j and (i + j == target):
                return True

    print("Failed num (part 1):", target)
    return False


nums = get_data()
preamble = 25
pos = preamble # start position at preamble

reached_target = True
while reached_target:
    target = nums[pos]
    prev_nums = nums[pos-preamble:pos]
    reached_target = check_sum(nums=prev_nums, target=target)
    pos += 1


""" Part 2 """
invalid_number = 105950735

for n in range(2, 100):
    slice_n = n
    end_slice = nums.index(invalid_number) - slice_n

    for i in range(end_slice+1):
        nums_sliced = nums[i:i+slice_n]
        sum_slice = sum(nums_sliced)

        if sum_slice == invalid_number:
            print("Encryption weakness (part 2):",min(nums_sliced) + max(nums_sliced))
            quit() # Stop program
        elif sum_slice > invalid_number:
            break
