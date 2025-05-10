import random

class Table:
    def __init__(self):
        self.table = [' '] * 9
    def print_table(self):
        print("ПОЛЕ")
        for i in range(3):
            row = self.table[i*3:(i+1)*3]
            print(f"| {row[0]} | {row(1)} | {row(2)} |")
    def print_table_nums(self):
        print("Номера клітинок:")
        for i in range(3):
            row = [str(place) for place in range]
            print(f"| {row[0]} | {row(1)} | {row(2)} |")
            print()
    def is_full(self):
        return ' ' not in self.table

    def get_table(self):
        return self.table

class Game:
    def __init__(self):
        self.table = Table()
        self.winner = None
    def make_move(self, square, letter):

class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        move = None
        while move not in game.available_moves:
            try:
                move = int(input(f"Хід {self.letter}. Виберіть позицію від 0 до 8"))
            except ValueError:
                continue
            return move

class Bot:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
        move = random.choice(game.available_moves())
        print(f"Бот ({self.letter}) вибирає: {move}")
        return move

def play():
    game = Game()
    player = Player('X')
    bot = Bot('0')

    game.print_table_nums()
    game.print_table()

    while True: