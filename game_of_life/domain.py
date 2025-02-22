from typing import List, Tuple, Literal, Union

World = List[List[Union[Literal["-"], Literal["o"]]]]


def _neighbors_of(coordinates: Tuple[int, int], world: World):
    x, y = coordinates
    adjacents_x = x - 1, x, x + 1
    adjacents_y = y - 1, y, y + 1

    return [
        (i, j)
        for i in adjacents_x
        for j in adjacents_y
        if 0 <= i < len(world)
        and 0 <= j < len(world[i])
        and world[i][j] == "o"
        and (i, j) != coordinates
    ]


def _next_tile_when_dead(position: Tuple[int, int], world: World):
    i, y = position
    cell = world[i][y]
    assert cell == "-"

    return "o" if len(_neighbors_of(position, world)) == 3 else "-"


def _next_tile_when_alive(position: Tuple[int, int], world: World):
    i, y = position
    cell = world[i][y]
    assert cell == "o"

    neighbors = _neighbors_of(position, world)
    match len(neighbors):
        case 0 | 1 | 4 | 5 | 6 | 7 | 8:
            return "-"
        case 2 | 3:
            return "o"
        case _:
            raise ValueError('received invalid length:', len(neighbors))


def _next_tile(position: Tuple[int, int], world: World):
    i, y = position
    return (
        _next_tile_when_alive(position, world)
        if world[i][y] == "o"
        else _next_tile_when_dead(position, world)
    )


def tick(world: World):
    return [
        [_next_tile((i, y), world) for y in range(len(world[i]))]
        for i in range(len(world))
    ]
