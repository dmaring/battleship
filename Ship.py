"""
Ship class for battleship game
"""


class Ship:

    def __init__(self, x: int, y: int, direction: str, length: int):
        # direction True = vertical, direction False = horizontal
        self.coords = []
        if direction.lower() == 'vert':
            for i in range(length):
                self.coords.append((x, y + i))
        elif direction.lower() == 'hor':
            for i in range(length):
                self.coords.append(tuple([x + i, y]))
        self.health = length

    def print_coords(self):
        print(self.coords)

    def dec_health(self, amount=1: int):
        if self.health:
            self.health -= 1
        else:
            #TODO sink ship
            print("Ship is sunk!")
