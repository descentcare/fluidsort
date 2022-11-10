#!/usr/bin/env python3
from game import (
        Board,
        BoardDisplay
    )
import random
from time import sleep

class Bot():
    def __init__(self, board):
        self.board = board
        self.moves = []

    def move_valid(self, source, destination):
        return (len(self.board.choices[source]) == 0 
            or len(self.board.choices[destination]) == self.board.fluid_level
            or source == destination)

    def _move(self, source, destination):
        if self.move_valid(source, destination):
            return False
        self.moves.append((source, destination))
        self.board.move(source, destination)
        return True

class FullRandomBot(Bot):
    def move(self):
        return self._move(*map(lambda c: c.letter, random.choices(self.board.cups, k=2)))

class RandomBot(Bot):
    def move(self):
        source = random.choice(list(filter(lambda c: len(c) > 0 and not c.closed(), self.board.cups))).letter
        destination = random.choice(list(filter(lambda c: not c.full() and c.letter != source,
                                           self.board.cups))).letter
        print(source, destination, sep='|')
        print('\n'*10)
        return self._move(source, destination)

def main():
    board = Board('qwert', 4)
    tui = BoardDisplay(board)
    bot = RandomBot(board)
    while not board.win():
        tui.display()
        bot.move()
    tui.display()
    print(f"Won in {len(bot.moves)} moves")

if __name__=="__main__":
	main()

