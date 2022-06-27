# Day 3
import pandas as pd

def get_data():
    # Read data from text file into df
    df = pd.read_table("day_3_data.txt", dtype="object", header=None)
    # Split each binary string into individual character bits
    df = df[0].str.split('', expand=True)
    # Remove the first and last column as these are empty
    df.drop(columns=[0, df.columns[-1]], inplace=True)

    return df


def part1(df):
    num_cols = df.shape[1]

    # Gets the most common bit for each column
    gamma_rate = [df[i].mode()[0] for i in range(1, num_cols+1)]
    # Epsilon rate is the inverse bits of the gamma rate binary string
    epsilon_rate = ['1' if i == '0' else '0' for i in gamma_rate]

    # Convert binary lists to decimal values
    gamma_rate_decimal = int("".join(gamma_rate), 2)
    epsilon_rate_decimal = int("".join(epsilon_rate), 2)

    print("Part1:", gamma_rate_decimal*epsilon_rate_decimal)


df = get_data()
part1(df)
