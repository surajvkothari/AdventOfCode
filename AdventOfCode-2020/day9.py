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

    print(target)
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
