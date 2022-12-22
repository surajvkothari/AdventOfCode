# Advent of code 2021
# Day 3

import pandas as pd

def get_data():
    num_cols = 12

    # Read tabular data into a dataframe
    df = pd.read_fwf("day_3_data.txt", widths=[1]*num_cols, header=None, dtype="object")

    return df


def part1(df):
    num_cols = df.shape[1]

    # Gets the most common bit for each column
    gamma_rate = [df[i].mode()[0] for i in range(0, num_cols)]
    # Epsilon rate is the inverse bits of the gamma rate binary string
    epsilon_rate = ['1' if i == '0' else '0' for i in gamma_rate]

    # Convert binary lists to decimal values
    gamma_rate_decimal = int("".join(gamma_rate), 2)
    epsilon_rate_decimal = int("".join(epsilon_rate), 2)

    print("Part1:", gamma_rate_decimal*epsilon_rate_decimal)


df = get_data()
part1(df)
