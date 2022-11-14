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

    def move_invalid(self, source, destination):
        return (self.board.choices[source].empty()
            or self.board.choices[destination].full()
            or source == destination)

    def _move(self, source, destination):
        if self.move_invalid(source, destination):
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
        return self._move(source, destination)

class ClosingRandomBot(Bot):
    def move(self):
        for c1 in self.board.cups:
            for c2 in self.board.cups:
                if (c1.letter == c2.letter or
                     c1.empty() or c2.full() or c1.closed() or c2.closed()):
                    continue
                if c2.one_colored() and c1.cup[-1] == c2.cup[0]:
                    return self._move(c1.letter, c2.letter)
        source = random.choice(list(filter(lambda c: len(c) > 0 and not c.closed(), 
                                           self.board.cups))).letter
        destination = random.choice(list(filter(lambda c: not c.full() and c.letter != source,
                                           self.board.cups))).letter
        return self._move(source, destination)

class ClosingWithPreviousBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_move = None

    def move(self):
        for c1 in self.board.cups:
            for c2 in self.board.cups:
                if (c2.letter, c1.letter) == self.previous_move:
                    continue
                if (c1.letter == c2.letter or
                     c1.empty() or c2.full() or c1.closed() or c2.closed()):
                    continue
                if c2.one_colored() and c1.cup[-1] == c2.cup[0]:
                    self.previous_move = c1.letter, c2.letter
                    return self._move(c1.letter, c2.letter)
        source = random.choice(list(filter(lambda c: len(c) > 0 and not c.closed(), 
                                           self.board.cups))).letter
        destination = random.choice(list(filter(lambda c: not c.full() and c.letter != source,
                                           self.board.cups))).letter
        self.previous_move = c1.letter, c2.letter
        return self._move(source, destination)

def main():
    board = Board('qwerasdf', 9)
    tui = BoardDisplay(board)
    bot = ClosingWithPreviousBot(board)
    while not board.win():
        #tui.display()
        bot.move()
    tui.display()
    print(f"Won in {len(bot.moves)} moves")

if __name__=="__main__":
	main()

