# Day 3
import pandas as pd

def get_data():
    with open("day_3_data.txt") as f:
        # Removes newline character and splits binary string into individual bits
        binary = [list(line.strip()) for line in f]

    print(binary)
    df = pd.DataFrame(binary, dtype="object")  # 2D list into pd dataframe
    
    num_cols = df.shape[1]

    # Gets the most common bit for each column
    gamma_rate = [df[i].mode()[0] for i in range(num_cols)]
    # Epsilon rate is the inverse bits of the gamma rate binary string
    epsilon_rate = ['1' if i == '0' else '0' for i in gamma_rate]

    # Convert binary lists to decimal values
    gamma_rate_decimal = int("".join(gamma_rate), 2)
    epsilon_rate_decimal = int("".join(epsilon_rate), 2)

    print("Part1:", gamma_rate_decimal*epsilon_rate_decimal)


def part1(binary):
    pass


binary = get_data()
part1(binary)
