import random

WIN_COMBOS = [
    [0,1,2], [3,4,5], [6,7,8],  # rows
    [0,3,6], [1,4,7], [2,5,8],  # cols
    [0,4,8], [2,4,6]            # diagonals
]

def get_move(board):
    #Simple heuristic: win > block > center > corners > sides#

    # 1. Try to win
    for combo in WIN_COMBOS:
        vals = [board[i] for i in combo]
        if vals.count("O") == 2 and vals.count(" ") == 1:
            return combo[vals.index(" ")]

    # 2. Block opponent
    for combo in WIN_COMBOS:
        vals = [board[i] for i in combo]
        if vals.count("X") == 2 and vals.count(" ") == 1:
            return combo[vals.index(" ")]

    # 3. Center
    if board[4] == " ":
        return 4

    # 4. Corners
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        return random.choice(corners)

    # 5. Sides
    sides = [i for i in [1,3,5,7] if board[i] == " "]
    return random.choice(sides) if sides else None