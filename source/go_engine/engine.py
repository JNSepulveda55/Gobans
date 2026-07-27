            
"""Implementation of a GO engine following GTP2

TODO: Create a test suite
NOTE: This first implementation will use naive algorithms
"""

from dataclasses import dataclass
from pprint import pprint

from utils import make_empty_board  # , preprocess_input
# from admin_commands import 


# Board and stones
DEFAULT_SIZE = 19
LETTER_MAPPINGS = {chr(i+64): i for i in range(1, 9)} | {chr(i+64): i-1 for i in range(10, 27)}
BLACK_INT, BLACK_STR = -1, "B"
WHITE_INT, WHITE_STR = 1, "W"
EMPTY_INT = 0
STR2INT_COLOR = {BLACK_STR: BLACK_INT, WHITE_STR: WHITE_INT}
INT2STR_COLOR = {BLACK_INT: BLACK_STR, WHITE_INT: WHITE_STR}


@dataclass
class Vertex:
    """A vertex is a coordinate with a letter and a number"""
    letter: str  # A to Z, excluding I
    number: int  # 1 to 25

    def __repr__(self):
        return self.letter + self.number


@dataclass
class Move:
    """A move is a color and a Vertex"""
    color: str  # B or W
    vertex: Vertex

    def __repr__(self):
        return self.color + " " + str(self.vertex)


class Engine:
    """Engine based on GTP2"""

    def __init__(self):
        """Initialize an Engine object"""
        self.board_size: int = DEFAULT_SIZE  # We should later support (width, height)
        self.board_configuration: list[list[int]] = make_empty_board(self.board_size)
        self.captured_by_white: int = 0
        self.captured_by_black: int = 0
        self.move_history:list[Move] = []
        self.komi: int = 6.5
        # self.time_settings  # Currently not supported

    # ----------------- Private Methods ----------------- #
    def _place_stone(self, move: Move) -> None:
        color = move.color
        letter = move.vertex.letter
        number = move.vertex.number

        # Internal coordinates
        x = LETTER_MAPPINGS[letter] - 1
        y = self.board_size - number  # Same as self.board_size - (number - 1) - 1

        # Check if the vertex is empty
        assert self.board_configuration[y][x] == EMPTY_INT, "illegal move"

        self.board_configuration[y][x] = STR2INT_COLOR[color]

        # TODO: Handle self-capture
        # TODO: Handle capturing
        # TODO: Handle ko
        # TODO: Handle super ko







    # ----------------- Setup Commands ----------------- #
    def clear_board(self) -> None:
        """The board is cleared, the number of captured stones is
        reset to zero for both colors and the move history is reset
        to empty."""
        self.board_configuration = make_empty_board(self.board_size)
        self.captured_by_white = 0
        self.captured_by_black = 0
        self.move_history = []

    def boardsize(self, size: int) -> None:
        """The board size is changed. For simplicity, in our engine
        this also clears the board. Our implementation"""
        assert type(size) is int, "Syntax error: unacceptable Size" 
        assert (0 < size <= 25), "Syntax error: unacceptable Size"
        self.board_size = size
        self.clear_board()

    def komi(self, new_komi: float) -> None:
        assert type(new_komi) is float, "Syntax error: unacceptable Size"
        self.komi = new_komi


def main() -> None:

    engine = Engine()
    engine.boardsize(9)
    pprint(engine.board_configuration)
    print("-"*100)

    move = Move("W", Vertex("A", 1))
    engine._place_stone(move)
    
    move = Move("B", Vertex("B", 1))
    engine._place_stone(move)

    pprint(engine.board_configuration)

    # Illegal move since that space is
    # move = Move("W", Vertex("A", 1))
    # engine._place_stone(move)

    pprint(engine.board_configuration)



if __name__ == "__main__":
    main()
