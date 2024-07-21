import os
import time

from game_of_life.animation import render_frame
from game_of_life.domain import World, tick


def game_of_life(seed: World):
    assert len(seed) == len(seed[1])

    current = seed
    while True:
        render_frame(current)
        current = tick(current)
        time.sleep(0.8)


if __name__ == "__main__":
    game_of_life(
        [
            ["o", "-", "o", "-", "o", "-"],
            ["-", "o", "-", "o", "-", "o"],
            ["o", "-", "o", "-", "o", "-"],
            ["-", "o", "-", "o", "-", "o"],
            ["o", "-", "o", "-", "o", "-"],
            ["-", "o", "-", "o", "-", "o"],
        ]
    )
