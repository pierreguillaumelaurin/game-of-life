import os
import time

from game_of_life.domain import World, tick


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def render(world: World):
    clear_terminal()

    output = ""
    for row in world:
        for cell in row:
            output += cell

        output += "\n"

    print(output)


def game_of_life(seed: World):
    assert len(seed) == len(seed[1])
    current = seed
    while True:
        render(current)
        current = tick(current)
        time.sleep(0.8)


if __name__ == "__main__":
    game_of_life([
        ['o', '-', 'o', '-', 'o', '-'],
        ['-', 'o', '-', 'o', '-', 'o'],
        ['o', '-', 'o', '-', 'o', '-'],
        ['-', 'o', '-', 'o', '-', 'o'],
        ['o', '-', 'o', '-', 'o', '-'],
        ['-', 'o', '-', 'o', '-', 'o'],
    ])
