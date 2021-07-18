from random import choice
from classes import Guess, Player
from words import game_words


class Game:

    def __init__(self):
        self.guesses = []
        self.game_word = choice(game_words)
        self.guessed_string = " _ " * len(self.game_word)

    def get_player_guess(self):
        letter = Player.guess_attempt()
        if any(letter == guess.letter for guess in self.guesses):
            raise Exception
        elif letter not in self.game_word:
            return Guess(letter, "miss")
        return Guess(letter, "hit")

    def resolve_game_status(self):
        bad_guesses = [guess for guess in self.guesses if guess.play == "miss"]
        if len(bad_guesses) == len(self.game_word):
            pass
        good_guesses = [guess for guess in self.guesses if guess.play == "hit"]
        hangman_string = ""
        for letter in self.game_word:
            if any(letter == guess.letter for guess in good_guesses):
                hangman_string += f"{letter} "
            else:
                hangman_string += "_ "
        return hangman_string.strip()







def main():
    while True:
        game = Game()
        while True:
            x = game.resolve_games_status()
            if x:
                break
            else:
                self.guessed_word = x
            try:
                player_guess = game.get_player_guess()
            except Exception as e:
                print(e)
                continue
            if player_guess.is_hit():
                pass
