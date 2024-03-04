
import numpy as np
import random



class board():

    def __init__(self):
        self.board = np.array([[1, 2, 3], 
                               [4, 5, 6], 
                               [7, 8, None]])
        self.px = 2 # position x-coord
        self.py = 2 # position y-coord

    def find_legal_moves(self):
        legal_moves = []
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

            if 0 <= self.px + dx < self.board.shape[0] and \
               0 <= self.py + dy < self.board.shape[1]:
                legal_moves.append((dx, dy))
        return legal_moves

    def shuffle(self, n=1):

        for _ in range(n):

            # Find Legal Moves
            legal_moves = self.find_legal_moves()
            dx, dy = random.choice(legal_moves)

            # Change Board
            self.board[self.px, self.py] = self.board[self.px + dx, self.py + dy]
            self.board[self.px + dx, self.py + dy] = None

            # Move Position
            self.px = self.px + dx
            self.py = self.py + dy








