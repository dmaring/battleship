from Ship import Ship, Destroyer, Carrier, Battleship, Submarine, Direction


class Board:
    def __init__(self):
        self.screen = [[0 for x in range(10)] for y in range(10)]
        self.ships_remaining = 0
        self.fleet = []

    def display_board(self):
        for x in range(len(self.screen)):
            # for y in range(len(self.screen)):
            print(self.screen[x])

    def fill_board(self, symbol):
        for ship in self.fleet:
            for x, y in ship.coords:
                if self.validate_placement(x, y) == False:
                    print("not a valid placement")
                    break
                else:
                    self.screen[x][y] = symbol

    def validate_hit(self, x, y):
        if self.screen[x][y] != 0:
            for ship in self.fleet[:]:
                for coord in ship.coords:
                    if coord == (x, y):
                        print("hit!")
                        self.screen[x][y] = 'X'
                        ship.dec_health()
                        if ship.health == 0:
                            self.ships_remaining -= 1
                            self.fleet.remove(ship)
                        self.display_board()
                        return True
        return False

    def add_ship(self, x, y, direction, length, player):
        print("adding ship(s)...")
        ship_dict = {
            "1": Destroyer,
            "2": Submarine,
            "3": Battleship,
            "4": Carrier
        }
        ship_const = ship_dict.get(length)
        self.fleet.append(ship_const(int(x), int(y), direction))
        self.ships_remaining += 1
        symbol = ''
        if player == 1:
            symbol = "1"
        else:
            symbol = "2"
        self.fill_board(symbol)
        self.display_board()

    def validate_placement(self, x, y):
        if self.screen[x][y] != 0:
            return False
        return True


class Player:
    def __init__(self, player_num: int):
        self.name = "Player " + str(player_num)
        self.board = Board()


class Game:
    def __init__(self):
        self.p1 = Player(1)
        self.p2 = Player(2)
        self.current_player = self.p1
        self.opponent = self.p2

    def start_game(self):
        if self.current_player.board.ships_remaining == 0:
            self.initialize_ships(1)
            self.toggle_turn()
            self.initialize_ships(2)
        game_on = True
        while game_on:
            self.toggle_turn()
            x, y = self.get_user_input()
            hit = self.opponent.board.validate_hit(int(x), int(y))
            if hit and self.check_victory():
                game_on = False
            self.display_score()

    def get_user_input(self):
        print()
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

    def initialize_ships(self, player: int):
        # print("Player 1, how many ships would you like to start off with?")
        print("======================")
        print("NEW GAME")
        print("======================")
        print(f"{self.current_player.name}")
        x = input("Give x coordinate: ")
        y = input("Give y coordinate: ")
        d = input("Which direction? (v or h): ")
        direction = None
        if (d == "v"):
            direction = Direction.vertical
        elif (d == "h"):
            direction = Direction.horizontal
        l = input(
            "What type of ship?\n1) Destroyer\n2) Submarine\n3) Battleship \n4) Carrier\n")
        self.current_player.board.add_ship(x, y, direction, l, player)

    def display_score(self):
        print("\n======================")
        print("Current score:")
        print(f"Player 1 has {self.p1.board.ships_remaining} remaining ships.")
        print(f"Player 2 has {self.p2.board.ships_remaining} remaining ships.")
        print("======================\n")


g = Game()
g.start_game()
