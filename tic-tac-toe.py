from abc import ABC
import game
class Players(ABC):
    def __init__(self):
        self.moves = []
        self.order = 0
    def __getitem__(self, item):
        return self.moves[item]
    def __len__(self):
        return len(self.moves)

class Human(Players):
    def __init__(self):
        super().__init__()
        self.sign = "X"
    def choose_move(self):
        move = game.ask_question("Choose your next move's index: ", 0, 9)
        return move
    def win(self):
        print("____COMPUTER____")
        print("NOOOOOOOO WHY SILLY HUMAN HAS WON???!")
    def add(self, move):
        self.moves.append(move)

class Computer(Players):
    def __init__(self):
        super().__init__()
        self.sign = "O"
    def choose_move(self):
        import random
        move = random.randrange(0, 9)
        return move
    def win(self):
        print("____COMPUTER____")
        print("HAHAHAHHAHAHHAHAHHHAHAHAHAHAH I BEAT YOU MAN")
    def add(self, move):
        print("____COMPUTER____")
        print("Now it's my turn!")
        self.moves.append(move)

class Board:
    def __init__(self):
        self.board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def __len__(self):
        return len(self.board)
    def __getitem__(self, item):
        return self.board
    def __setitem__(self, key, value):
        self.board[key] = value
        return self.board
    def show_board(self):
        for square, value in enumerate(self.board):
            if (square+1)%3==0:
                print(f'{value}')  # As the string ends, it prints the line
                print("__________")
            else:
                print(f'{value} | ', end='')

class Game:
    def __init__(self):
        self.human = Human()
        self.computer = Computer()
        self.combinations = ([0, 1, 2],
                             [3, 4, 5],
                             [6, 7, 8],
                             [6, 4, 2],
                             [0, 4, 8],
                             [0, 3, 6],
                             [1, 4, 7],
                             [2, 5, 8]
                             )
        self.table = Board()
        self.players = [self.human, self.computer]
        self.results = []
        self.squares = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def ask_move(self):  # (!)
        move = None
        while move not in self.squares:  # If the selected square has already been an str
            move = self.players[0].choose_move()
        self.squares.remove(move)
        self.players[0].add(move)
        self.change_board(self.players[0])
        self.change_combinations(move)

    def change_board(self, player):
        for move in range(len(player.moves)):
            for number in range(len(self.table.board)):  # Because it is a tender method, we define .board, as it is obj
                if player.moves[move] == self.table.board[number]:
                    self.table.board[number] = player.sign

    def change_combinations(self, move):  # ()  As it was, nothing changed
        player = self.players[0]
        for round in range(len(self.combinations)):  # checking parentheses
            for number in range(len(self.combinations[round])):
                if move == self.combinations[round][number]:
                    self.combinations[round][number] = player.sign

    def checking_three(self, player):  # !
        result = False
        for list in self.combinations:
            for num in list:  # Checks every list, if there aren't three X or O, then returns False
                if num == player.sign:
                    self.results.append(num)
            if len(self.results) == 3:
                result = True
            else:
                self.results = []
        self.results = []
        return result

    def squares_ended(self):  # !
        return len(self.squares) == 0

    def order(self):  # !
        self.players.reverse()

    def game(self):
        victory = "Draft"  # The initial, and if the .checking_three returned nothing
        while not self.squares_ended():
            print()
            self.table.show_board()
            if len(self.players[1].moves) >= 3:
                if self.checking_three(self.players[1]):
                    victory = self.players[1].win()
                    break
            elif len(self.players[0].moves) >= 3:
                if self.checking_three(self.players[0]):
                    victory = self.players[0].win()
                    break
            self.ask_move()
            self.order()
        return victory
game_c = Game()
game_c.game()
