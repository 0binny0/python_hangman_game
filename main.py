from string import ascii_lowercase as accepted_letters
from random import choice
from classes import Guess, Player
from words import game_words, hangmans
from sys import exit
from time import sleep
import os


class Game:

    def __init__(self):
        self.guesses = []
        self.word = choice(game_words)
        self.guessed_string = " _ " * len(self.word)

    def get_player_guess(self):
        letter = Player.guess_attempt()
        if any(letter == guess.letter for guess in self.guesses):
            raise Exception("That letter was already guessed. Guess again.\n")
        elif letter not in self.word:
            return Guess(letter, "miss")
        return Guess(letter, "hit")

    def resolve_game_status(self):
        bad_guesses = [guess for guess in self.guesses if guess.play == "miss"]
        if bad_guesses and len(bad_guesses) == 5:
            print('\n' + hangmans[5])
            print(f"You have no more guesses. The word was {self.word}.")
            return False
        bad_letters = ', '.join(
            list(map(lambda guess: guess.letter, bad_guesses))
        )
        print(f"""
            {hangmans[len(bad_guesses)]}

            BAD GUESSES: [{bad_letters}]

            WORD TO GUESS: {self.guessed_string}
        """)
        if "_" not in self.guessed_string:
            sleep(2)
            exit()
        else:
            return True

    def update_guessed_word(self, guess):
        self.add_guess(guess)
        good_guesses = [
            guess for guess in self.guesses if guess.play == "hit"
        ]
        hangman_string = ""
        for letter in self.word:
            if any(letter == guess.letter for guess in good_guesses):
                hangman_string += f"{letter} "
            else:
                hangman_string += "_ "
        self.guessed_string = hangman_string.strip()
        word = self.guessed_string.replace(" ", "").replace("_", "*")
        return word


    def add_guess(self, guess):
        return self.guesses.append(guess)


def main():
    while True:
        game = Game()
        while True:
            player_can_guess = game.resolve_game_status()
            if not player_can_guess:
                sleep(2)
                exit()
            try:
                player_guess = game.get_player_guess()
            except Exception as e:
                print(e)
                sleep(2)
                os.system('cls' if os.name=='nt' else 'clear')
                continue
            os.system('cls' if os.name=='nt' else 'clear')
            if player_guess.is_hit():
                guessed_word = game.update_guessed_word(player_guess)
                if guessed_word == game.word:
                    print(f"You win! You guessed the word {game.word} right!")
            else:
                misses = game.add_guess(player_guess)

if __name__ == '__main__':
    os.system('cls' if os.name=='nt' else 'clear')
    main()
