from abc import abstractmethod
from abc import ABC
import game
class Players(ABC):
    def __init__(self):
        self.moves = []
        self.order = 0
    @abstractmethod
    def choose_move(self):
        pass
    def __getitem__(self, item):
        return self.moves[item]

class Human(Players):
    def __init__(self):
        super().__init__()
        self.sign = "X"
    def choose_move(self):
        move = game.ask_question("Choose your next move's index(0-8): ", 0, 9)
        self.moves.append(move)
        return move
    def win(self):
        print("NOOOOOOOO WHY SILLY HUMAN HAS WON???!")

class Computer(Players):
    def __init__(self):
        super().__init__()
        self.sign = "O"
    def choose_move(self):
        import random
        move = random.randrange(0, 9)
        self.moves.append(move)
        return move
    def win(self):
        print("HAHAHAHHAHAHHAHAHHHAHAHAHAHAH I BEAT YOU MAN")

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
        self.players = [self.human, self.computer]
        self.results = None

    def ask_move(self):  # !
        move = self.players[0].choose_move()
        self.change_combinations(move)

    def change_combinations(self, move):  # ()
        player = self.players[0]
        for round in range(len(self.combinations)):  # checking parentheses
            for combination in range(len(self.combinations[round])):
                if move == self.combinations[round][combination]:
                    self.combinations[round][combination] = player.sign

    def checking_three(self, player):  # We check two of players, ()
        self.results = []
        for round in range(len(self.combinations)):
            if player.sign in self.combinations[round]:
                for number in range(len(self.combinations[round])):
                    if player.sign == self.combinations[round][number]:
                        self.results.append(player.sign)
        return self.results

    def completed_combinations(self, player):  # !
        is_won = self.checking_three(player)
        if len(is_won)==3:  # If the array is full of signs, it means, that we save it and define a winner
            return True
        else:
            self.results = []

    def squares_ended(self):  # !
        self.results = []
        for rounds in range(len(self.combinations)):
            for number in range(len(self.combinations[rounds])):
                if self.combinations[rounds][number] == str:
                    self.results.append(number)
        if len(self.results) == 8:
            return True
        else:
            self.results = []
            return False

    def order(self):  # !
        self.players.reverse()

    def game(self):
        while not self.squares_ended():
            if self.completed_combinations(self.players[1]):
                self.players[1].win()
                break
            elif self.completed_combinations(self.players[0]):
                self.players[0].win()
                break
            self.ask_move()
            if self.squares_ended():
                print("The human and computer has received a draft!")
                break
            self.order()

game_c = Game()
game_c.game()
