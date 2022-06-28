# Day 4
import numpy as np

class BingoBoard():
    def __init__(self, rows):
        self.rows = np.array(rows)

    def convert_to_int(self, rows):
        """ Converts string data into integers """
        return np.array([[int(i) for i in row] for row in rows])

    def get_sum_unmarked(self):
        """ Gets the sum of all unmarked numbers """
        # Get the list of numbers not marked
        unmarked_nums = self.rows[self.rows != 'X']
        unmarked_nums = unmarked_nums.astype('int')  # Convert array to int

        return sum(unmarked_nums)

    def check_bingo(self, row_index, col_index):
        """ Checks the row and column given for a bingo """

        row = self.rows[row_index]
        col = self.rows[:,col_index]

        # Check if the whole row or column is just 'X'
        return (np.all(row == 'X') or np.all(col == 'X'))

    def mark_num(self, num):
        """
        Marks off the given number in the board if it is present
        and returns if a Bingo has occured
        """

        row_index, col_index = None, None
        # Find the num in the board
        for i, row in enumerate(self.rows):
            for j, n in enumerate(row):
                if n == num:
                    self.rows[i,j] = 'X'  # Mark it by replacing with 'X'

                    row_index, col_index = i, j  # Store the row and column of the marked num

        # Check both indexes are valid
        if (row_index, col_index) != (None, None):
            return self.check_bingo(row_index, col_index)
        else:
            return False


def get_data():
    with open("day_4_data.txt") as f:
        numbers_draw = f.readline().split(',')

        bingo_boards_raw = []  # Raw bingo data from text file
        bingo_board = None
        for line in f:
            if line == '\n':
                # If bingo board is not None
                if bingo_board:
                    bingo_boards_raw.append(bingo_board)

                # Reset the bingo board
                bingo_board = []
            else:
                bingo_board.append(line.split())

        bingo_boards_raw.append(bingo_board)  # Append the final bingo board

    bingo_boards = []
    for bingo in bingo_boards_raw:
        # Create a new bingo board class
        bingo_boards.append(BingoBoard(bingo))


    return numbers_draw, bingo_boards


def part1(numbers_draw, bingo_boards):
    for num in numbers_draw:
        for bingo_board in bingo_boards:
            is_bingo = bingo_board.mark_num(num)

            if is_bingo:
                print("Part 1:", int(num)*bingo_board.get_sum_unmarked())
                return


def part2(numbers_draw, bingo_boards):
    num_bingo_boards = len(bingo_boards)
    boards_with_bingo = bingo_boards.copy()

    for num in numbers_draw:
        for bingo_board in bingo_boards:
            is_bingo = bingo_board.mark_num(num)

            if is_bingo:
                # Remove the bingo board from the list if it got a bingo
                if bingo_board in boards_with_bingo:
                    boards_with_bingo.remove(bingo_board)

                    # Use the result of the bingo from the last board remaining
                    if len(boards_with_bingo) == 0:
                        print("Part 2:", int(num)*bingo_board.get_sum_unmarked())
                        return


numbers_draw, bingo_boards = get_data()
part1(numbers_draw, bingo_boards)

numbers_draw, bingo_boards = get_data()
part2(numbers_draw, bingo_boards)
