#!/usr/bin/env python3

# Inspired by Numberphile - The Light Switch Problem (Youtube)
# https://www.youtube.com/watch?v=-UBDRX6bk-A
#
# This is a bruge-force method, but there's another "more mathy"
# way to determine the value at each switch. If the prime
# factorization of a switch is even, then the switch is even,
# then the light is on. If the prime factorization of a switch
# is odd, then the light is off.


def main():
    # Initialize board
    board = {i: False for i in range(1, 101)}

    # Loop through each person flipping switches
    # Person 7 flips every 7th switch
    for step in range(1,101):

        # Flip light at every step, step*2, step*3, ...
        for i in range(step, 101, step):
            board[i] ^= True

        print(f"=== After {step} ===")
        output_board(board)


# terminal colors
ON = "\033[1;37m"
OFF = "\033[1;30m"
RESET = "\033[0m";

# Output
def output_board(board):
    on_line = 0
    for k, v in board.items():
        color = ON if v else OFF
        print(f"{color}{k:>3}{RESET}", end=" ")
        on_line += 1

        # 10 on a row
        if on_line >= 10:
            print()
            on_line = 0

if __name__ == "__main__":
    main()
