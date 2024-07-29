import os
from typing import List


def _clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def render_frame(grid: List[List[str]]):
    _clear_terminal()

    output = ""
    for row in grid:
        output += "".join(row)
        output += "\n"

    print(output)
