import random

def get_move(board):
    #Choose a random empty spot
    empty = [i for i, v in enumerate(board) if v == " "]
    return random.choice(empty) if empty else None