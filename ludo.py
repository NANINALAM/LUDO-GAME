import random

class LudoGame:
    def __init__(self):
        self.board_size = 30 
        self.player_position = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, roll):
        self.player_position += roll
        if self.player_position > self.board_size:
            self.player_position = self.board_size 

    def play_turn(self):
        input("Press Enter to roll the dice...")
        roll = self.roll_dice()
        print(f"You rolled a {roll}!")
        self.move_player(roll)
        print(f"Your current position: {self.player_position}")

    def check_winner(self):
        if self.player_position == self.board_size:
            print("Congratulations! You reached the goal and won!")
            return True
        return False

def main():
    game = LudoGame()
    print("Welcome to the simplified Ludo game!")
    print(f"Your goal is to reach position {game.board_size}.")
    
    while not game.check_winner():
        game.play_turn()
    
    print("Game over!")

if __name__ == "__main__":
    main()
