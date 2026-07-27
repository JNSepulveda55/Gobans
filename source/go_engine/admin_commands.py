# Engine
VERSION_NUMBER = 2
ENGINE_NAME = "Gobans"

# ----------------- Administrative Commands ----------------- #
def protocol_version() -> int:
    return VERSION_NUMBER

def name() -> str:
    return ENGINE_NAME

# def version() -> str:  # Not supported yet

# def known_command(command_name: str) -> bool:  # Not supported yet

# def list_commands() -> str:  # Not supported yet

# def quit() -> str:  # Not supported yet