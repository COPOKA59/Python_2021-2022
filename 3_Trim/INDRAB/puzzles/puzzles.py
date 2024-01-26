from typing import List, Any

import pygame

from data.level import Level
from data.flask import Flask


# puzzles
def get_puzzle(puzzle_id: int):
    for puzzle in PUZZLES:
        if puzzle.num_id == puzzle_id:
            return puzzle
    return None


puzzle_id = 0


def add_puzzle(puz: Level):
    global puzzle_id
    puz.num_id = puzzle_id
    PUZZLES.append(puz)
    story.append(False)
    puzzle_id += 1


story = []

PUZZLES: list[Level] = []
# 0
add_puzzle(Level(True, [
    Flask(['CYAN', 'CYAN']),
    Flask(['CYAN', 'CYAN'])
], 2, 2))  # всего колб, пустые

# 1
add_puzzle(Level(True, [
    Flask(['ORANGE', 'ORANGE', 'BROWN', 'RED']),
    Flask(['BEIGE', 'MINT_GREEN', 'MINT_GREEN', 'BROWN']),
    Flask(['ORANGE', 'RED', 'MINT_GREEN', 'MINT_GREEN']),
    Flask(['BEIGE', 'RED', 'RED', 'BEIGE']),
    Flask(['BROWN', 'ORANGE', 'BEIGE', 'BROWN']),
    Flask([]),
    Flask([])
], 7, 2))

# 2
add_puzzle(Level(True, [
    Flask(['ORANGE', 'PINK', 'CYAN', 'GRAY']),
    Flask(['PINK', 'MINT_GREEN', 'MINT_GREEN', 'GRAY']),
    Flask(['ORANGE', 'BLUE', 'ORANGE', 'BLUE']),
    Flask(['BLUE', 'MINT_GREEN', 'CYAN', 'PINK']),
    Flask(['BLUE', 'MINT_GREEN', 'CYAN', 'RED']),
    Flask(['RED', 'GRAY', 'GRAY', 'CYAN']),
    Flask(['PINK', 'RED', 'ORANGE', 'RED']),
    Flask([]),
    Flask([])
], 9, 2))

# 3
add_puzzle(Level(False, [
    Flask(['CYAN', 'BLUE', 'CYAN', 'ORANGE']),
    Flask(['ORANGE', 'DARK_GREEN', 'MINT_GREEN', 'PINK']),
    Flask(['PINK', 'PINK', 'GRAY', 'CYAN']),
    Flask(['BLUE', 'VIOLET', 'MINT_GREEN', 'DARK_GREEN']),
    Flask(['RED', 'GRAY', 'DARK_GREEN', 'CYAN']),
    Flask(['PINK', 'GRAY', 'VIOLET', 'MINT_GREEN']),
    Flask(['RED', 'VIOLET', 'DARK_GREEN', 'ORANGE']),
    Flask(['ORANGE', 'MINT_GREEN', 'RED', 'BLUE']),
    Flask(['BLUE', 'GRAY', 'RED', 'VIOLET']),
    Flask([]),
    Flask([])
], 11, 2))

# 4
add_puzzle(Level(False, [
    Flask(['CYAN', 'DARK_GREEN', 'BLUE', 'GRAY']),
    Flask(['CYAN', 'CYAN', 'GREEN', 'MINT_GREEN']),
    Flask(['GREEN', 'RED', 'VIOLET', 'ORANGE']),
    Flask(['MINT_GREEN', 'RED', 'ORANGE', 'VIOLET']),
    Flask(['CYAN', 'ORANGE', 'GRAY', 'DARK_GREEN']),
    Flask(['DARK_GREEN', 'VIOLET', 'BROWN', 'YELLOW']),
    Flask(['DARK_GREEN', 'GRAY', 'PINK', 'PINK']),
    Flask(['RED', 'RED', 'ORANGE', 'GREEN']),
    Flask(['PINK', 'GRAY', 'BROWN', 'VIOLET']),
    Flask(['YELLOW', 'MINT_GREEN', 'BROWN', 'YELLOW']),
    Flask(['BROWN', 'YELLOW', 'GREEN', 'MINT_GREEN']),
    Flask(['BLUE', 'PINK', 'BLUE', 'BLUE']),
    Flask([]),
    Flask([])
], 14, 2))

# 5
add_puzzle(Level(False, [
    Flask(['ORANGE', 'CYAN', 'VIOLET', 'VIOLET']),
    Flask(['PINK', 'CYAN', 'GREEN', 'BLUE']),
    Flask(['GRAY', 'GREEN', 'PINK', 'CYAN']),
    Flask(['GRAY', 'MINT_GREEN', 'RED', 'GREEN']),
    Flask(['GREEN', 'PINK', 'RED', 'VIOLET']),
    Flask(['ORANGE', 'MINT_GREEN', 'BLUE', 'ORANGE']),
    Flask(['CYAN', 'GRAY', 'RED', 'PINK']),
    Flask(['BLUE', 'RED', 'GRAY', 'ORANGE']),
    Flask(['MINT_GREEN', 'MINT_GREEN', 'BLUE', 'VIOLET']),
    Flask([]),
    Flask([])
], 11, 2))

# 6
add_puzzle(Level(False, [
    Flask(['CYAN', 'BLUE', 'GRAY', 'CYAN']),
    Flask(['MINT_GREEN', 'RED', 'BLUE', 'PINK']),
    Flask(['BLUE', 'MINT_GREEN', 'PINK', 'BLUE']),
    Flask(['ORANGE', 'GRAY', 'RED', 'CYAN']),
    Flask(['MINT_GREEN', 'CYAN', 'ORANGE', 'MINT_GREEN']),
    Flask(['RED', 'ORANGE', 'PINK', 'RED']),
    Flask(['GRAY', 'GRAY', 'PINK', 'ORANGE']),
    Flask([]),
    Flask([])
], 9, 2))

# 7
add_puzzle(Level(False, [
    Flask(['BLUE', 'GRAY', 'RED', 'CYAN']),
    Flask(['MINT_GREEN', 'BLUE', 'RED', 'MINT_GREEN']),
    Flask(['PINK', 'CYAN', 'BLUE', 'MINT_GREEN']),
    Flask(['PINK', 'MINT_GREEN', 'RED', 'RED']),
    Flask(['PINK', 'ORANGE', 'CYAN', 'GRAY']),
    Flask(['CYAN', 'PINK', 'ORANGE', 'GRAY']),
    Flask(['GRAY', 'BLUE', 'ORANGE', 'ORANGE']),
    Flask([]),
    Flask([])
], 9, 2))

# 8
add_puzzle(Level(False, [
    Flask(['RED', 'GRAY', 'GREEN', 'GRAY']),
    Flask(['BROWN', 'DARK_GREEN', 'BLUE', 'CYAN']),
    Flask(['YELLOW', 'PINK', 'RED', 'ORANGE']),
    Flask(['CYAN', 'BLUE', 'GREEN', 'GREEN']),
    Flask(['VIOLET', 'BLUE', 'BLUE', 'MINT_GREEN']),
    Flask(['CYAN', 'DARK_GREEN', 'VIOLET', 'GRAY']),
    Flask(['CYAN', 'VIOLET', 'MINT_GREEN', 'BROWN']),
    Flask(['ORANGE', 'DARK_GREEN', 'MINT_GREEN', 'RED']),
    Flask(['GRAY', 'BROWN', 'BROWN', 'ORANGE']),
    Flask(['GREEN', 'DARK_GREEN', 'PINK', 'YELLOW']),
    Flask(['RED', 'MINT_GREEN', 'ORANGE', 'YELLOW']),
    Flask(['PINK', 'VIOLET', 'YELLOW', 'PINK']),
    Flask([]),
    Flask([])
], 14, 2))

# 9
add_puzzle(Level(False, [
    Flask(['MINT_GREEN', 'GRAY', 'ORANGE', 'YELLOW']),
    Flask(['RED', 'PURPLE', 'GREEN', 'CYAN']),
    Flask(['GREEN', 'PINK', 'MINT_GREEN', 'PURPLE']),
    Flask(['YELLOW', 'PINK', 'RED', 'BROWN']),
    Flask(['GREEN', 'VIOLET', 'BROWN', 'PURPLE']),
    Flask(['GREEN', 'GRAY', 'PURPLE', 'YELLOW']),
    Flask(['ORANGE', 'GRAY', 'CYAN', 'DARK_GREEN']),
    Flask(['RED', 'DARK_GREEN', 'CYAN', 'PINK']),
    Flask(['VIOLET', 'VIOLET', 'CYAN', 'MINT_GREEN']),
    Flask(['DARK_GREEN', 'BROWN', 'PINK', 'ORANGE']),
    Flask(['GRAY', 'MINT_GREEN', 'YELLOW', 'ORANGE']),
    Flask(['RED', 'BROWN', 'DARK_GREEN', 'VIOLET']),
    Flask([]),
    Flask([])
], 14, 2))
