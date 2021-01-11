# Welcome to this strange version of tic-tac-toe game!
# The rules here are so oversimplified - 
# the human moves first, as he has "X",
# the computer moves after, it has "O".
# To simplify the understanding of method's role, 
# I'll introduce you definition of marks here:
# ! - Means that it is used in main cycle
# (method's name) - Means that it is called inside the method 

from abc import ABC
import game
class Players(ABC):
    def __init__(self):
        self.moves = []
    def __getitem__(self, item):
        return self.moves[item]
    def __len__(self):
        return len(self.moves)

class Human(Players):
    def __init__(self):
        super().__init__()
        self.sign = "X"
    def choose_move(self):  # (.ask_move())
        move = game.ask_question("Choose your next move's index: ", 0, 9)
        return move
    def win(self):  # !
        print("____COMPUTER____")
        print("NOOOOOOOO WHY SILLY HUMAN HAS WON???!")
    def add(self, move):  # (.ask_move())
        self.moves.append(move)

class Computer(Players):
    def __init__(self):
        super().__init__()
        self.sign = "O"
    def choose_move(self):  # (.ask_move())
        import random
        move = random.randrange(0, 9)
        return move
    def win(self):  # !
        print("____COMPUTER____")
        print("HAHAHAHHAHAHHAHAHHHAHAHAHAHAH I BEAT YOU MAN")
    def add(self, move):  # (.ask_move())
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
    def show_board(self):  # !
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}", end="\n")
        print("----------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}", end="\n")
        print("----------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}", end="\n")


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

    def ask_move(self):  # !
        move = None
        while move not in self.squares:  # If the selected square has already been an str
            move = self.players[0].choose_move()
        self.squares.remove(move)
        self.players[0].add(move)
        self.change_board(self.players[0])
        self.change_combinations(move)

    def change_board(self, player):  # (.ask_move())
        for move in range(len(player.moves)):
            for number in range(len(self.table.board)):  # Because it is a tender method, we define .board, as it is obj
                if player.moves[move] == self.table.board[number]:
                    self.table.board[number] = player.sign

    def change_combinations(self, move):  # (.ask_move())
        player = self.players[0]
        for round in range(len(self.combinations)):  # checking parentheses
            for number in range(len(self.combinations[round])):
                if move == self.combinations[round][number]:
                    self.combinations[round][number] = player.sign

    def checking_three(self, player):  # !
        result = False
        for list in self.combinations:
            for num in list:  
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

    def game(self):  # Here is a cycle 
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
