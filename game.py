#!/usr/bin/env python3
import random

class FluidCup():
    def __init__(self, fluid_level, letter=None):
        self.cup = []
        self.letter = letter
        self.fluid_level = fluid_level

    def __len__(self):
        return len(self.cup)

    def pour(self, source_cup):
        if self.letter == source_cup.letter:
            return
        while True:
            if len(self) == self.fluid_level or len(source_cup) == 0:
                break
            x = source_cup.cup.pop()
            self.cup.append(x)
            if len(source_cup) and source_cup.cup[-1] != x:
                break
    def closed(self):
        '''
        winning position of a cup
        '''
        return self.empty() or self.full() and self.one_colored()

    def empty(self):
        return len(self) == 0

    def full(self):
        return len(self) == self.fluid_level

    def one_colored(self):
        return all(map(lambda c: c == self.cup[0], self.cup))

class BoardDisplay():
    COLOR_SPACES = [
            "\033[48;2;255;0;0m \033[0m",
            "\033[48;2;0;255;0m \033[0m",
            "\033[48;2;0;0;255m \033[0m",
            "\033[48;2;255;255;0m \033[0m",
            "\033[48;2;255;0;255m \033[0m",
            "\033[48;2;0;255;255m \033[0m",
            "\033[48;2;255;255;255m \033[0m",
            "\033[48;2;120;60;255m \033[0m",
        ]
    def __init__(self, board):
        self.board = board
        self.letter_colors = dict()
        if len(board.letters)-1 > len(BoardDisplay.COLOR_SPACES):
            for l in board.letters:
                self.letter_colors[l] = l
        else:
            for i in range(len(board.letters)-1):
                self.letter_colors[board.letters[i]] = BoardDisplay.COLOR_SPACES[i]
        self.letter_colors[' '] = ' '

    def display(self):
        print('\033[2J\033[2;H\033[m', end='')
        print(''.join(f' {{{x}}} ' for x in self.board.letters))
        for fc in self.board.cups:
            print(' ┏━┓ ' if fc.full() and fc.one_colored() else ' '*5,end='')
        print()
        for i in range(self.board.fluid_level-1, -1, -1):
            row = []
            for c in self.board.cups:
                if len(c) > i:
                    row.append(c.cup[i])
                else:
                    row.append(' ')
            print(''.join(f' ┃{self.letter_colors[x]}┃ ' for x in row))
        print(' ┗━┛ ' * len(row)) 

class Board():
    def __init__(self, letters, fluid_level):
        self.letters = letters
        self.fluid_level = fluid_level
        fluid = list(letters[:-1]) * fluid_level
        random.shuffle(fluid)
        self.cups = [FluidCup(fluid_level, x) for x in letters]
        while fluid:
            c = random.choice(self.cups)
            if len(c) < fluid_level:
                c.cup.append(fluid.pop())
        self.choices = dict()
        for c in self.cups:
            self.choices[c.letter] = c

    def move(self, source, destination):
        self.choices[destination].pour(self.choices[source])

    def win(self):
        return all(map(lambda c: c.closed(), self.cups))

if __name__ == "__main__":
    fluid_level = 0
    while not (1 < fluid_level < 10):
        fluid_level = int(input("choose fluid level[2-9]: "))
    letters = ''
    while len(letters) < 3 or len(letters) > len(set(letters)):
        letters = input("Enter your controll scheme:")
    board = Board(letters, fluid_level)
    tui = BoardDisplay(board)

    turns = 0
    while not board.win():
        tui.display()
        player_input = input("\nEnter 2 letters (source destination): ")
        if len(player_input) != 2:
            continue
        source, destination = player_input
        if source == destination or source not in board.letters or destination not in board.letters:
            continue
        board.move(source, destination)
        turns += 1
    tui.display()
    print(f"\nYou win in {turns} turns")
