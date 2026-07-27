# Escape Sequences
INVALID_SCAPE_SEQUENCES = {chr(i): None for i in range(32) if i not in (9, 10)}
TAB = chr(9)  # TAB is also known as HF


# ---------------------- Helper Functions ---------------------- #
def make_empty_board(board_size: list[int, int]) -> list[list[int]]:
    return [[0]*board_size for _ in range(board_size)]


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