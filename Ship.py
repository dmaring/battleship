"""
Ship class for battleship game
"""
from enum import Enum

class Direction(Enum):
    vertical = 1
    horizontal = 2


class Ship:
    def __init__(self, x: int, y: int, direction: Direction, length: int):
        self.coords = []
        if direction == Direction.vertical:
            for i in range(length):
                self.coords.append((x, y + i))
        else:
            for i in range(length):
                self.coords.append((x + i, y))
        self.health = length

    def print_coords(self):
        print(self.coords)

    def dec_health(self, amount=1):
        if self.health:
            self.health -= 1
        else:
            #TODO sink ship
            print("Ship is sunk!")


class Carrier(Ship):
    def __init__(self, x, y, direction: Direction):
        self.length = 5
        super().__init__(x, y, direction, self.length)


class Battleship(Ship):
    def __init__(self, x, y, direction: Direction):
        self.length = 4
        super().__init__(x, y, direction, self.length)


class Submarine(Ship):
    def __init__(self, x, y, direction: Direction):
        self.length = 3
        super().__init__(x, y, direction, self.length)


class Destroyer(Ship):
    def __init__(self, x, y, direction: Direction):
        self.length = 5
        super().__init__(x, y, direction, self.length)
