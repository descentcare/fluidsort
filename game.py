#!/usr/bin/env python3
import random

color_spaces = [
        "\033[48;2;255;0;0m \033[0m",
        "\033[48;2;0;255;0m \033[0m",
        "\033[48;2;0;0;255m \033[0m",
        "\033[48;2;255;255;0m \033[0m",
        "\033[48;2;255;0;255m \033[0m",
        "\033[48;2;0;255;255m \033[0m",
        "\033[48;2;255;255;255m \033[0m",
        "\033[48;2;120;60;255m \033[0m",
        ]

fluid_level = 0
while not (1 < fluid_level < 10):
    fluid_level = int(input("choose fluid level[2-9]: "))
letters = ''
while ' ' in letters or len(letters) < 3 or len(letters) > len(set(letters)):
    letters = input("Enter your controll scheme:")

class FluidCup():
    def __init__(self, letter=None):
        self.cup = []
        if letter is None:
            self.letter = ' '
        else:
            self.letter = letter
            #self.cup = [letter] * fluid_level

    def __len__(self):
        return len(self.cup)

    def pour(self, source_cup):
        if self.letter == source_cup.letter:
            return
        while True:
            if len(self) == fluid_level or len(source_cup) == 0:
                break
            x = source_cup.cup.pop()
            self.cup.append(x)
            if len(source_cup) and source_cup.cup[-1] != x:
                break
    def closed(self):
        return len(self) == 0 or all(map(lambda c: c == self.cup[0], self.cup)) and len(self) == fluid_level

def init_board(letters):
    fluid = list(letters) * fluid_level
    random.shuffle(fluid)
    board = [FluidCup(x) for x in letters] + [FluidCup()]
    while fluid:
        c = random.choice(board)
        if len(c) < fluid_level:
            c.cup.append(fluid.pop())
    return board

board = init_board(letters)
letter_colors = dict()
if len(letters) > len(color_spaces):
    for l in letters:
        letter_colors[l] = l
else:
    for i in range(len(letters)):
        letter_colors[letters[i]] = color_spaces[i]
letters += ' '
letter_colors[' '] = ' '

choices = dict()
for c in board:
    choices[c.letter] = c

ub='┗━┛'
def print_board(board):
    print('\033[2J\033[2;H\033[m', end='')
    print(''.join(f' {{{x}}} ' for x in letters))
    print()
    for i in range(fluid_level-1, -1, -1):
        row = []
        for c in board:
            if len(c) > i:
                row.append(c.cup[i])
            else:
                row.append(' ')
        print(''.join(f' ┃{letter_colors[x]}┃ ' for x in row))
    print(' ┗━┛ ' * len(row)) 
turns = 0
while True:
    print_board(board)
    player_input = input("\nEnter 2 letters (source destination): ")
    if len(player_input) != 2:
        continue
    source, destination = player_input
    if source == destination or source not in letters or destination not in letters:
        continue
    source = choices[source]
    destination = choices[destination]
    destination.pour(source)
    turns += 1
    if all(map(lambda c: c.closed(), board)):
        print_board(board)
        print(f"\nYou win in {turns} turns")
        break
