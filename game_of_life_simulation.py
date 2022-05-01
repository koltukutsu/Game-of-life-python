from collections import namedtuple, defaultdict
import random
import time

Cell = namedtuple("Cell", ["x", "y"])


def getNeighbors(cell):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                yield Cell(x, y)


def getNeighborCount(board):
    neighbor_counts = defaultdict(int)
    for cell in board:
        for neighbor in getNeighbors(cell):
            neighbor_counts[neighbor] += 1

    return neighbor_counts


def advanceBoard(board):
    new_board = set()
    for cell, count in getNeighborCount(board).items():
        if count == 3 or (cell in board and count == 2):
            new_board.add(cell)

    return new_board


def generateBoard(desc):
    board = set()
    for row, line in enumerate(desc.split("\n")):
        for col, elem in enumerate(line):
            if elem == "X":
                board.add(Cell(int(col), int(row)))

    return board


def boardToString(board, pad=0):
    if not board:
        return "empty"
    board_str = ""
    xs = [x for (x, _) in board]
    ys = [y for (_, y) in board]

    for y in range(min(ys) - pad, max(ys) + 1 + pad):
        for x in range(min(xs) - pad, max(xs) + 1 + pad):
            board_str += "X" if Cell(x, y) in board else "."
        board_str += "\n"

    return board_str.strip()


if __name__ == "__main__":
    while True:
        try:
            _RANDOMNESS = int(input("Say Yes(1) or No(0) to Randomness: \n\n  >"))
            if _RANDOMNESS == 1 or _RANDOMNESS == 0:
                break
            else:
                raise TypeError
        except:
            print("\nChoose 1 or 0.")
        else:
            break

    CHOICES = ".X"
    WEIGHTS = [0.5, 0.5]  # change it if you do not want the probs equal
    COLS = 120
    ROWS = 30

    _SLEEP_TIME = 0
    ITERATIONS = 2000
    if _RANDOMNESS == 1:
        state = [
            "".join(random.choices(CHOICES, weights=WEIGHTS, k=COLS))
            for _ in range(ROWS)
        ]
        state = "\n".join(state)
    else:
        state = """...XX...X.
        XX.XX.....
        .X.XX..XXX
        .X.XX..XXX
        .X.XX..XXX
        .X.XX..XXX
        """
    f = generateBoard(state)
    for _ in range(ITERATIONS):
        f = advanceBoard(f)
        print("\033[2J\033[1;1H" + boardToString(f, 2))
        time.sleep(_SLEEP_TIME)
