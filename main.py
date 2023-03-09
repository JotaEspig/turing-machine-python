#!/usr/bin/python3.8

# Explanation: https://en.wikipedia.org/wiki/Turing_machine

STATES = {'right', 'carry', 'done'}
TAPE_ALPHABET_SYMBOLS = {'', '0', '1'}
BLANK_SYMBOL = ''
INPUT_SYMBOLS = {'0', '1'}
INITIAL_STATE = 'right'
FINAL_STATE = 'done'

# Move tape
R = 0
L = 1


def action(write_symbol: str, move_tape: int, next_state: str) -> None:
    pass


def add_one(input: str) -> None:
    pass


def main() -> None:
    print("hello")


if __name__ == "__main__":
    main()
