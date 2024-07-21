import os
import time
from typing import List, Literal, Tuple
import sys

World = List[List[Literal["-", "o"]]]


def neighbors_of(coordinates: Tuple[int, int], world: World):
    x, y = coordinates
    adjacents_x = x - 1, x, x + 1
    adjacents_y = y - 1, y, y + 1

    return [
        (i, j)
        for i in adjacents_x
        for j in adjacents_y
        if i < len(world) and j < len(world[i]) and world[i][j] == 'o' and (i, j) != coordinates
    ]


def next_tile_when_dead(position: Tuple[int, int], world: World):
    i, y = position
    cell = world[i][y]
    assert cell == '-'

    return 'o' if len(neighbors_of(position, world)) == 3 else world[i][y]


def next_tile_when_alive(position: Tuple[int, int], world: World):
    i, y = position
    cell = world[i][y]
    assert cell == 'o'

    match len(neighbors_of(position, world)):
        case 0 | 1 | 4 | 5 | 6 | 7 | 8:
            return '-'
        case 2 | 3:
            return 'o'


def next_tile(position: Tuple[int, int], world: World):
    i, y = position
    return next_tile_when_alive(position, world) if world[i][y] == 'o' else next_tile_when_dead(position, world)


def tick(world: World):
    return [[next_tile((i, y), world) for y in range(len(world[i]))] for i in range(len(world))]


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
