from string import ascii_lowercase as accepted_letters

class Player:

    @staticmethod
    def guess_attempt():
        guess = input(
            "Guess a letter that falls within the mystery word...\n>>> "
        ).lower()
        while guess not in accepted_letters:
            guess = input("You didn't guess a letter. Think hard!...\n>>> ")
        return guess


class Guess:
    def __init__(self, letter, play):
        self.letter = letter
        self.play = play

    def is_hit(self):
        if self.play == "hit":
            return True
        return False
