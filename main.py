#!/usr/bin/python3.8

# Explanation about Turing Machine:
# https://en.wikipedia.org/wiki/Turing_machine
#
# This Turing Machine basically just adds one to a binary number
# e.g.  01 -> 010
#       10 -> 011
#       11 -> 100
#
# Please take note that since the "infinite tape" is physically impossible,
# this code "simulates" the "infinite tape" adding 2 blanks symbols, one at the
# beginning and another at the end.

import sys


# 7-tuple 
STATES = {"right", "carry", "done"}
TAPE_ALPHABET_SYMBOLS = {"", "0", "1"}
BLANK_SYMBOL = ""
INPUT_SYMBOLS = {"0", "1"}
INITIAL_STATE = "right"
FINAL_STATE = "done"

# Move tape
R = 0 # Right
L = 1 # Left

tape = []
current_symbol_idx = 0
state = INITIAL_STATE


def action(write_symbol: str, move_tape: int, next_state: str) -> None:
    global tape, current_symbol_idx, state
    tape[current_symbol_idx] = write_symbol
    current_symbol_idx += 1 if move_tape == R else -1
    state = next_state


def transition_function():
    symbol = tape[current_symbol_idx]

    if state == "right":
        if symbol == "0" or symbol == "1":
            action(symbol, R, state)
        elif symbol == BLANK_SYMBOL:
            action("", L, "carry")

    elif state == "carry":
        if symbol == "1":
            action("0", L, state)
        elif symbol == "0" or symbol == "":
            action("1", L, "done")

    elif state == FINAL_STATE:
        return


def main() -> None:
    global tape, current_symbol_idx

    # Converts into list and adds blank symbols
    tape = list(sys.argv[1])
    tape.insert(0, "")
    tape.append("")
    current_symbol_idx = 1 # To previne the code to read the first blank symbol

    while True:
        transition_function()
        if state == FINAL_STATE:
            break

    tape_str = "".join(tape)
    print(f"Final tape: {tape_str}")


if __name__ == "__main__":
    main()
