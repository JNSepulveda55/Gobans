            
"""Implementation of a GO engine following GTP2"""

from dataclasses import dataclass

# Engine
VERSION_NUMBER = 2
ENGINE_NAME = "Gobans"

# Escape Sequences
INVALID_SCAPE_SEQUENCES = {chr(i): None for i in range(32) if i not in (9, 10)}
TAB = chr(9)  # TAB is also known as HF

# Board and stones
DEFAULT_SIZE = 19
LETTER_MAPPINGS = {chr(i+64): i for i in range(1, 9)} | {chr(i+64): i-1 for i in range(10, 27)}
BLACK_INT, BLACK_STR = -1, "B"
WHITE_INT, WHITE_STR = 1, "W"
EMPTY_INT = 0



# ---------------------- Helper Functions ---------------------- #
def make_empty_board(board_size: list[int, int]) -> list[list[int]]:
    return [[0]*board_size[0] for _ in range(board_size[1])]


def preprocess_input(input: str) -> str:

    # 1. Remove all control characters except TAB and LF
    input.translate(str.maketrans(INVALID_SCAPE_SEQUENCES))

    # 2. Remove all comments
    comments = []
    in_comment = False
    for char in input:
        if char == "#" and not in_comment:  # Found a comment
            comment = ""
            in_comment = True

        if char == "\n" and in_comment:  # Comments end on line breaks
            in_comment = False  
            comments.append(comment)

        if in_comment:
            comment += char

    for comment in comments:
        input = input.replace(comment, "")

    # 3. Replace all TABs with SPACEs
    input = input.replace(TAB, " ")

    # 4. Discard any empty lines
    lines = input.split("\n")
    input = "\n".join([line for line in lines if (line != "" and set(line) != {" "})])

    return input


# ----------------- Administrative Commands ----------------- #
def protocol_version() -> int:
    return VERSION_NUMBER

def name() -> str:
    return ENGINE_NAME

# def version() -> str:  # Not supported yet

# def known_command(command_name: str) -> bool:  # Not supported yet

# def list_commands() -> str:  # Not supported yet

# def quit() -> str:  # Not supported yet


@dataclass
class Vertex:
    """A vertex is a coordinate with a letter and a number"""
    letter: str  # A to Z, excluding I
    number: str  # 1 to 25

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
        y = number - 1

        # Remember to handle ko






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

    input = """
@dataclass
class Vertex:
    letter: str  # A to Z, excluding I
    number: str  # 1 to 25

    def __repr__(self):
        return self.letter + self.number


@dataclass
class Move:
    color: str  # B or W
    vertex: Vertex

    def __repr__(self):
        return self.color + " " + str(self.vertex)


class Engine:

    def __init__(self):
        self.board_size: list = [9, 9]  # (width, height)
        self.board_configuration: list[list[int]] = make_empty_board(self.board_size)
        self.captured_by_white: int = 0
        self.captured_by_black: int = 0
        self.move_history:list[Move] = []
        self.komi: int = 6.5
        # self.time_settings  # Currently not supported
    """
    print(LETTER_MAPPINGS)



if __name__ == "__main__":
    main()
