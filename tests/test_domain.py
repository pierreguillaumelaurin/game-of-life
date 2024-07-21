from game_of_life.domain import tick


def test_should_return_alive_cell_when_dead_cell_surrounded_by_3():
    next_state = tick([
        ['-', 'o', '-'],
        ['o', '-', 'o'],
        ['-', '-', '-'],
    ])

    assert next_state[1][1] == 'o'

def test_should_return_dead_cell_when_alive_cell_surrounded_by_less_than_2():
    next_state = tick([
        ['-', '-', '-'],
        ['o', 'o', '-'],
        ['-', '-', '-'],
    ])

    assert next_state[1][1] == '-'

def test_should_return_alive_cell_when_alive_cell_surrounded_by_2():
    next_state = tick([
        ['-', '-', '-'],
        ['o', 'o', 'o'],
        ['-', '-', '-'],
    ])

    assert next_state[1][1] == 'o'

def test_should_return_alive_cell_when_alive_cell_surrounded_by_3():
    next_state = tick([
        ['-', 'o', '-'],
        ['o', 'o', 'o'],
        ['-', '-', '-'],
    ])

    assert next_state[1][1] == 'o'

def test_should_return_dead_cell_when_alive_cell_surrounded_by_more_than_3():
    next_state = tick([
        ['-', 'o', '-'],
        ['o', 'o', 'o'],
        ['-', '-', 'o'],
    ])

    assert next_state[1][1] == '-'
