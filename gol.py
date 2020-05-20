import matplotlib.pyplot as plt
import time
import random
import copy
import numpy as np


def random_state(width, height):
    boardstate = []
    for i in range(height):
        boardstate.append([])
        n = 0
        while n < width:
            randomnumber = random.random()
            if randomnumber >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            boardstate[i].append(cell_state)
            n += 1

    return boardstate


def next_board_state(initial_state):
    next_state = copy.deepcopy(initial_state)
    for i in range(0, len(initial_state)):
        for j in range(0, len(initial_state[i])):

            # handle edge cases
            a = j + 1
            b = j - 1
            c = i + 1
            d = i - 1

            if a > len(initial_state[i])-1:
                a = 0
            if b < 0:
                b = (len(initial_state[i])-1)
            if c > len(initial_state)-1:
                c = 0
            if d < 0:
                d = (len(initial_state)-1)

            top_neighbors = initial_state[d][a] + \
                initial_state[d][b] + initial_state[d][j]
            bottom_neighbors = initial_state[c][a] + \
                initial_state[c][b] + initial_state[c][j]
            right_neighbors = initial_state[i][a]
            left_neighbors = initial_state[i][b]

            sum_neighbors = top_neighbors + bottom_neighbors + left_neighbors + right_neighbors

            if initial_state[i][j] == 1:
                # Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
                if sum_neighbors <= 1:
                    next_state[i][j] = 0
                # Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
                elif sum_neighbors == 3 or sum_neighbors == 2:
                    next_state[i][j] = 1
                # Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
                elif sum_neighbors > 3:
                    next_state[i][j] = 0
            if initial_state[i][j] == 0:
                # Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
                if sum_neighbors == 3:
                    next_state[i][j] = 1

    return next_state


def render(a_random_state):
    for row in a_random_state:
        print(str(row).replace('1', '#').replace('0', ' ').replace(
            ',', '').replace('[', '').replace(']', ''))


while True:
    render(next_board_state(test))
    test = next_board_state(test)
    time.sleep(.2 - ((time.time() - starttime) % .2))
