Ship = __import__("Ship").Ship
Direction = __import__("Ship").Direction


class Board:
    def __init__(self):
        self.screen = [[0 for x in range(10)] for y in range(10)]
        self.ships_remaining = 0
        self.fleet = []

    def display_board(self):
        for x in range(len(self.screen)):
            # for y in range(len(self.screen)):
            print(self.screen[x])

    def fill_board(self):
        for ship in self.fleet:
            for x, y in ship.coords:
                self.screen[x][y] = 'X'

    def add_ship(self, num: int):
        # Code to add ship
        print("adding ship(s)...")
        s = Ship(0, 1, Direction.vertical, 2)
        s2 = Ship(7, 2, Direction.horizontal, 3)
        self.fleet.append(s)
        self.fleet.append(s2)
        self.ships_remaining += 1
        self.fill_board()
        self.display_board()


class Player:
    def __init__(self, player_num: int):
        self.name = "Player " + str(player_num)
        self.board = Board()


class Game:
    def __init__(self):
        self.p1 = Player(1)
        self.p2 = Player(2)
        self.current_player = self.p2
        self.opponent = self.p1

    def start_game(self):
        if self.current_player.board.ships_remaining == 0:
            self.initialize_ships()
        game_on = True
        while game_on:
            self.toggle_turn()
            x, y = self.get_user_input()
            hit = check_hit()
            if hit and self.check_victory():
                game_on = False
            self.display_score()

    def get_user_input(self):
        print("Current player: ***" + self.current_player.name + "***")
        x = y = ""
        while not x.isdigit():
            x = input("Please enter x coordinate: ")
        while not y.isdigit():
            y = input("Please enter y coordinate: ")
        print("firing at (" + x + ", " + y + ")!")
        return (x, y)

    def toggle_turn(self):
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1

    def check_victory(self):
        if self.opponent.board.ships_remaining == 0:
            return True

    def initialize_ships(self):
        print("Player 1, how many ships would you like to start off with?")
        count = input()
        self.p1.board.add_ship(count)
        print("Player 2, how many ships would you like to start off with?")
        count = input()
        self.p2.board.add_ship(count)

    def display_score(self):
        print("\n======================")
        print("Current score:")
        print(f"Player 1 has {self.p1.board.ships_remaining} remaining ships.")
        print(f"Player 2 has {self.p2.board.ships_remaining} remaining ships.")
        print("======================\n")


def check_hit():
    return True


g = Game()
g.start_game()
