"""Render the current GO state in the terminal"""

import sys

CHARS = {-1: "○", 0: "", 1: "●"}

#  ANSI escape sequences
CLEAR_SCREEN = "\x1b[2J"
CURSOR_HOME = "\x1b[H"

def make_empty_lines(rows: int, cols: int) -> None:
    """Make an empty rows x cols board.
    In Go, spaces are intersections, not squares"""
    
    top = ["┌────" + "┬────" * (cols-2) + "┐"]

    middle = ["│    " * (cols-1) + "│",
              "├────" + "┼────" * (cols-2) + "┤"]

    bot = ["│    " * (cols-1) + "│", 
           "└────" + "┴────" * (cols-2) + "┘"]
    return top + middle * (rows-2) + bot

def render_board(board_state: list[list[int]]) -> None:
    """Render the board in the terminal"""
    rows, cols = len(board_state), len(board_state[0])

    print(CLEAR_SCREEN)  # Clear the terminal
    lines = make_empty_lines(rows, cols)  # Initialize empty board

    for i, row in enumerate(board_state):
        for j, cell in enumerate(row):

            if cell == 0:  # Hardcoded for now
                continue

            line_i, line_j = 2*i, 5*j

            char = CHARS[cell]
            lines[line_i] = lines[line_i][:line_j] + char + lines[line_i][line_j+1:]

    sys.stdout.write(CURSOR_HOME + "\n".join(lines) + "\n")
    sys.stdout.flush()

    
def main() -> None:
    board_state = [
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  0,  0, -1,  0,  0,  1,  0],
    [ 0,  0,  1,  0, -1,  0,  1,  0,  0],
    [ 0,  0,  0,  1, -1,  1,  0,  0,  0],
    [ 0, -1, -1, -1,  0,  1,  1,  1,  0],
    [ 0,  0,  0, -1,  1,  0,  0,  0,  0],
    [ 0,  0, -1,  0,  0,  1,  0,  0,  0],
    [ 0, -1,  0,  0,  0,  0,  1,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
]
    render_board(board_state)

    input("Enter your next move: ")


if __name__ == "__main__":
    main()