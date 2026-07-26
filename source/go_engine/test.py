"""
NOTE:

- Moves will be received in Wa1 format. Internally they will be processed in SMG (Smart Game Format)

TO DO's
- [ ] Make board_state a class?
- [ ] Define notation for moves
- [ ] Go Text Protocol
"""


def make_empty_board_state(rows: int, cols: int) -> list[list[int]]:
    return [[0]*cols for _ in rows]


def make_move(board_state: list[list[int]], move: str) -> list[list[int]]:
    pass

def main() -> None:
    board = make_empty_board_state()
    print(board)


if __name__ == "__main__":
    main()