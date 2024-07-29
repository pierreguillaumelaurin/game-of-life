from time import sleep
from random import choice

from animation import render_frame
from domain import World, tick

GRID_LENGTH = 20


def game_of_life(seed: World):
    assert len(seed) == len(seed[1])

    current = seed
    while True:
        render_frame(current)
        current = tick(current)
        sleep(0.8)


if __name__ == "__main__":
    game_of_life(
        [[choice(['-', 'o']) for _ in range(GRID_LENGTH)] for __ in range(GRID_LENGTH)]
    )
