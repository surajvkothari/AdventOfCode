# Advent of code 2022
# Day 1

def get_data():
    with open("day_1_data.txt") as f:
        calorie_sums = []
        sample = []
        for line in f:
            # Check line is not blank
            if len(line) > 1:
                sample.append(int(line.strip()))
            else:
                # Calculate sum of sample
                calorie_sums.append(sum(sample))
                sample = []

    return calorie_sums


def part1(calorie_sums):
    print("Part 1:", max(calorie_sums))


def part2(calorie_sums):
    sorted_calories = sorted(calorie_sums, reverse=True)
    sum_top_3 = sum(sorted_calories[:3])  # Get sum of the 3 highest values
    print("Part 2:", sum_top_3)

calorie_sums = get_data()
part1(calorie_sums)
part2(calorie_sums)
